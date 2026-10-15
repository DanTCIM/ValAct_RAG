"""PDF → Markdown, locally via docling (MIT; no external API, no key).

docling runs in its own throwaway uv environment (`uv run --isolated --with`)
so its heavy deps (torch, transformers, newer httpx) never touch the app's
pinned requirements.txt. First run downloads the env + layout models (~1 min);
later runs reuse the uv / Hugging Face caches.

Equations come out as plain text, not LaTeX, and graphic section headers can
be missed; the Claude lint stage (md_review.py) is the check for anything that
converted badly.
"""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

DOCLING_SPEC = "docling==2.132.0"


def convert_pdf(pdf_path: Path, out_dir: Path) -> Path:
    pdf_path = Path(pdf_path)
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"  docling convert: {pdf_path.name}")
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            "uv", "run", "--no-project", "--isolated", "--python", "3.12",
            "--with", DOCLING_SPEC,
            "docling", "--to", "md", "--image-export-mode", "placeholder",
            "--output", tmp, str(pdf_path.resolve()),
        ]
        proc = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
        produced = Path(tmp) / (pdf_path.stem + ".md")
        if proc.returncode != 0 or not produced.is_file():
            raise RuntimeError(
                f"docling failed (exit {proc.returncode}): {proc.stderr[-2000:]}"
            )
        md = produced.read_text(encoding="utf-8")

    out_path = out_dir / (pdf_path.stem + ".md")
    out_path.write_text(md, encoding="utf-8")
    print(f"    wrote {out_path} ({len(md):,} chars)")
    return out_path
