from __future__ import annotations

import time

from valact.clients import get_voyage_client
from valact.settings import EMBED_MODEL


def embed_texts(
    texts: list[str],
    *,
    input_type: str = "document",
    model: str = EMBED_MODEL,
    retries: int = 4,
) -> list[list[float]]:
    delay = 1.0
    for attempt in range(retries):
        try:
            client = get_voyage_client()
            if client is None:
                raise RuntimeError("Voyage client unavailable (missing VOYAGE_API_KEY?)")
            resp = client.embed(texts=texts, model=model, input_type=input_type)
            return [list(v) for v in resp.embeddings]
        except Exception as exc:
            if attempt == retries - 1:
                raise
            print(f"  embed retry {attempt + 1}/{retries} after {delay:.1f}s ({exc})")
            time.sleep(delay)
            delay *= 2
    raise RuntimeError("unreachable")


def embed_query(query: str) -> list[float]:
    return embed_texts([query], input_type="query")[0]
