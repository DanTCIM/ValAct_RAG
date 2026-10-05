from __future__ import annotations

from typing import Iterable

from valact.embed import embed_texts
from valact.settings import EMBED_MODEL


def embed_iter(
    texts: Iterable[str],
    *,
    batch_size: int = 128,
    model: str = EMBED_MODEL,
) -> list[list[float]]:
    texts = list(texts)
    out: list[list[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        out.extend(embed_texts(batch, input_type="document", model=model))
    return out
