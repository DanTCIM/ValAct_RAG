from __future__ import annotations

from typing import Iterable

from valact.embed import embed_texts
from valact.settings import EMBED_MODEL, EMBED_PROVIDER


def embed_iter(
    texts: Iterable[str],
    *,
    batch_size: int | None = None,
    model: str = EMBED_MODEL,
    provider: str = EMBED_PROVIDER,
) -> list[list[float]]:
    if batch_size is None:
        batch_size = 128 if provider == "voyage" else 96
    texts = list(texts)
    out: list[list[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        out.extend(embed_texts(batch, input_type="document", model=model, provider=provider))
    return out
