"""Daily FRED yield/spread refresh: pull series from FRED, write parquet to Cloudflare R2.

Run locally:    python scripts/update_fred.py
Run in CI:      see .github/workflows/update_fred.yml
"""

import io
import os
import tomllib
from pathlib import Path

import boto3
import pandas as pd
from fredapi import Fred

BUCKET = "market-data"
KEY = "fred/yields.parquet"

SERIES_IDS = {
    "3 Month": "DGS3MO",
    "5 Year": "DGS5",
    "10 Year": "DGS10",
    "30 Year": "DGS30",
    "A Spread": "BAMLC0A3CA",
    "BBB Spread": "BAMLC0A4CBBB",
}

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
    fred = Fred(api_key=get_secret("FRED_API_KEY"))
    frames = [fred.get_series(code).rename(label).to_frame() for label, code in SERIES_IDS.items()]
    df = pd.concat(frames, axis=1)
    df.index.name = "Date"
    df = df.dropna(how="all").reset_index()
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
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
