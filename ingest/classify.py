from __future__ import annotations

import base64
import json
import re
from dataclasses import dataclass
from pathlib import Path

from valact.clients import get_anthropic_client
from valact.settings import ANTHROPIC_MODEL, COLLECTION_LABELS, COLLECTIONS

CLASSIFY_MAX_TOKENS = 400


@dataclass
class Suggestion:
    collection: str
    confidence: float
    reason: str


def _collection_catalog() -> str:
    lines = [f"- {k}: {COLLECTION_LABELS.get(k, k)}" for k in COLLECTIONS]
    return "\n".join(lines)


_SYSTEM = (
    "You categorize actuarial / accounting / regulatory documents into a fixed taxonomy. "
    "You return only JSON, never prose."
)


def _instruction() -> str:
    return (
        "Below is the list of valid collections (label after colon describes the topic):\n\n"
        f"{_collection_catalog()}\n\n"
        "Read only the title page and table of contents (typically the first 3-5 pages) of "
        "the attached PDF. Pick the SINGLE best collection.\n\n"
        'Return JSON: {"collection": "<one of the keys above>", '
        '"confidence": <0.0-1.0>, "reason": "<one short sentence>"}.\n'
        "If genuinely ambiguous, pick the closest match but report confidence below 0.7."
    )


def _strip_code_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9]*\n", "", text, count=1)
        text = re.sub(r"\n?```\s*$", "", text)
    return text


def suggest_collection(pdf_path: Path) -> Suggestion:
    pdf_path = Path(pdf_path)
    data = base64.standard_b64encode(pdf_path.read_bytes()).decode("utf-8")

    client = get_anthropic_client()
    resp = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=CLASSIFY_MAX_TOKENS,
        system=_SYSTEM,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": data,
                        },
                    },
                    {
                        "type": "text",
                        "text": _instruction(),
                        "cache_control": {"type": "ephemeral"},
                    },
                ],
            }
        ],
    )
    raw = "".join(
        block.text for block in resp.content if getattr(block, "type", None) == "text"
    )
    raw = _strip_code_fence(raw)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"suggest_collection: model returned non-JSON: {exc}\n---\n{raw[:500]}"
        ) from exc

    collection = str(payload.get("collection", "")).strip()
    if collection not in COLLECTIONS:
        # Fall back to lowest-confidence default; user can override.
        return Suggestion(
            collection=COLLECTIONS[0],
            confidence=0.0,
            reason=f"model returned unknown collection {collection!r}; defaulting",
        )

    try:
        confidence = float(payload.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    return Suggestion(
        collection=collection,
        confidence=max(0.0, min(1.0, confidence)),
        reason=str(payload.get("reason", "")).strip(),
    )
