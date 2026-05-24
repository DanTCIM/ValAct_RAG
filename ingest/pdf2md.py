from __future__ import annotations

import re
import time
from pathlib import Path

import requests

from valact.settings import get_secrets

MATHPIX_PDF_URL = "https://api.mathpix.com/v3/pdf"
POLL_INTERVAL_S = 2.0
POLL_TIMEOUT_S = 600.0

_IMG_LINK_RE = re.compile(r"!\[\]\((.*?)\)")


def _auth_headers() -> dict:
    s = get_secrets()
    if not s.mathpix_app_id or not s.mathpix_app_key:
        raise RuntimeError(
            "MathPix credentials missing. Set MATHPIX_APP_ID and MATHPIX_APP_KEY "
            "(or MATHPIX_API_KEY) in your .env or Streamlit secrets."
        )
    return {"app_id": s.mathpix_app_id, "app_key": s.mathpix_app_key}


def _submit(pdf_path: Path) -> str:
    options = (
        '{"conversion_formats": {"md": true}, '
        '"math_inline_delimiters": ["$", "$"], '
        '"rm_spaces": true}'
    )
    with pdf_path.open("rb") as fh:
        resp = requests.post(
            MATHPIX_PDF_URL,
            headers=_auth_headers(),
            data={"options_json": options},
            files={"file": fh},
            timeout=60,
        )
    resp.raise_for_status()
    body = resp.json()
    pdf_id = body.get("pdf_id")
    if not pdf_id:
        raise RuntimeError(f"MathPix submit returned no pdf_id: {body}")
    return pdf_id


def _wait_until_done(pdf_id: str) -> None:
    headers = _auth_headers()
    deadline = time.monotonic() + POLL_TIMEOUT_S
    while time.monotonic() < deadline:
        resp = requests.get(f"{MATHPIX_PDF_URL}/{pdf_id}", headers=headers, timeout=30)
        resp.raise_for_status()
        body = resp.json()
        status = body.get("status")
        if status == "completed":
            return
        if status == "error":
            raise RuntimeError(f"MathPix conversion errored: {body}")
        time.sleep(POLL_INTERVAL_S)
    raise TimeoutError(f"MathPix did not finish within {POLL_TIMEOUT_S}s (pdf_id={pdf_id})")


def _download_md(pdf_id: str) -> str:
    resp = requests.get(
        f"{MATHPIX_PDF_URL}/{pdf_id}.md", headers=_auth_headers(), timeout=60
    )
    resp.raise_for_status()
    return resp.text


def _normalize_image_links(md: str) -> str:
    def repl(match: re.Match) -> str:
        url = match.group(1)
        return f'<img src="{url}" alt="image" style="width:100%;height:auto;">'

    return _IMG_LINK_RE.sub(repl, md)


def convert_pdf(pdf_path: Path, out_dir: Path) -> Path:
    pdf_path = Path(pdf_path)
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"  mathpix submit: {pdf_path.name}")
    pdf_id = _submit(pdf_path)
    print(f"    pdf_id={pdf_id}, polling...")
    _wait_until_done(pdf_id)
    md = _download_md(pdf_id)
    md = _normalize_image_links(md)

    out_path = out_dir / (pdf_path.stem + ".md")
    out_path.write_text(md, encoding="utf-8")
    print(f"    wrote {out_path} ({len(md):,} chars)")
    return out_path
