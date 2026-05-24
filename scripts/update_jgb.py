"""Daily JGB yield refresh: pull MoF Japan CSVs, write parquet to Cloudflare R2.

Run locally:    python scripts/update_jgb.py
Run in CI:      see .github/workflows/update_jgb.yml
"""

import io
import os
import tomllib
from pathlib import Path

import boto3
import pandas as pd
from fredapi import Fred

BUCKET = "market-data"
KEY = "jgb/yields.parquet"
OUTPUT_TENORS = ["1Y", "10Y", "30Y", "40Y"]
FRED_FX_SERIES = "DEXJPUS"
FX_COLUMN = "JPY/USD"

JGB_ALL_CSV = "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/historical/jgbcme_all.csv"
JGB_REMOTE_CSV = "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"

_SECRETS_FILE = Path(__file__).resolve().parent.parent / ".streamlit" / "secrets.toml"


def get_secret(key: str) -> str:
    val = os.environ.get(key)
    if val:
        return val
    if _SECRETS_FILE.exists():
        with open(_SECRETS_FILE, "rb") as f:
            val = tomllib.load(f).get(key)
        if val:
            return val
    raise RuntimeError(f"Missing secret: {key}")


def build_df() -> pd.DataFrame:
    all_df = pd.read_csv(JGB_ALL_CSV, header=1, encoding="cp932")
    remote_df = pd.read_csv(JGB_REMOTE_CSV, header=1, encoding="cp932")
    df = pd.concat([all_df, remote_df]).drop_duplicates(subset=["Date"])
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df = df[["Date"] + OUTPUT_TENORS].sort_values("Date")
    for c in OUTPUT_TENORS:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    fred = Fred(api_key=get_secret("FRED_API_KEY"))
    fx = fred.get_series(FRED_FX_SERIES).rename(FX_COLUMN).to_frame()
    fx.index.name = "Date"
    fx = fx.reset_index()
    fx["Date"] = pd.to_datetime(fx["Date"])

    df = df.merge(fx, on="Date", how="left")
    df[FX_COLUMN] = df[FX_COLUMN].ffill()
    return df


def upload(df: pd.DataFrame) -> None:
    s3 = boto3.client(
        "s3",
        endpoint_url=f"https://{get_secret('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=get_secret("R2_ACCESS_KEY"),
        aws_secret_access_key=get_secret("R2_SECRET_KEY"),
    )
    buf = io.BytesIO()
    df.to_parquet(buf, index=False)
    s3.put_object(
        Bucket=BUCKET,
        Key=KEY,
        Body=buf.getvalue(),
        ContentType="application/octet-stream",
    )
    print(f"Uploaded {len(df)} rows to s3://{BUCKET}/{KEY}")


if __name__ == "__main__":
    upload(build_df())
