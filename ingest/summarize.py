from __future__ import annotations

import json
from pathlib import Path

from valact.clients import get_anthropic_client
from valact.settings import ANTHROPIC_MODEL, SUMMARY_PATH

SUMMARY_MAX_TOKENS = 1500

_INSTRUCTION = """You are summarizing an actuarial / accounting / regulatory document for a RAG corpus index.
Produce a single plain-text summary following this exact structure (no markdown headings, plain labels with colons):

Title: <document title>

Publisher and Published Date: <e.g., "Actuarial Standards Board, September 2001">

Purpose and Scope: <1-3 sentences>

Key Points:
- <bullet 1>
- <bullet 2>
- ...

Conclusions and Implications: <1-3 sentences>

Aim for 150-350 words total. Be concrete and faithful to the document; do not invent facts.
Return only the summary text, no preamble, no JSON, no code fences."""


def summarize_md(md_path: Path, collection: str, *, max_chars: int = 120_000) -> dict:
    md_text = Path(md_path).read_text(encoding="utf-8")
    if len(md_text) > max_chars:
        md_text = md_text[:max_chars] + "\n\n[... truncated for summary ...]"

    client = get_anthropic_client()
    resp = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=SUMMARY_MAX_TOKENS,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"# Document content\n\n{md_text}",
                        "cache_control": {"type": "ephemeral"},
                    },
                    {"type": "text", "text": _INSTRUCTION},
                ],
            }
        ],
    )
    summary = "".join(
        block.text for block in resp.content if getattr(block, "type", None) == "text"
    ).strip()
    if not summary:
        raise RuntimeError(f"summarize_md: empty summary returned for {md_path}")
    return {"collection_name": collection, "summary": summary}


def upsert_summary(
    filename_pdf: str,
    entry: dict,
    *,
    path: str | Path = SUMMARY_PATH,
) -> Path:
    path = Path(path)
    data: dict = {}
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
    data[filename_pdf] = entry
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding="utf-8")
    return path
