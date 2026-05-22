from __future__ import annotations

import json
from pathlib import Path

from valact.clients import get_pinecone_index
from valact.settings import PARENTS_PATH

from ingest.chunk import Chunk, Parent

PINECONE_TEXT_FIELD = "text"
PINECONE_BATCH = 100
PINECONE_META_MAX_BYTES = 38_000


def _truncate_text_for_meta(text: str, max_bytes: int = PINECONE_META_MAX_BYTES) -> str:
    encoded = text.encode("utf-8")
    if len(encoded) <= max_bytes:
        return text
    return encoded[:max_bytes].decode("utf-8", errors="ignore")


def delete_source(index_name: str | None, *, collection: str, source_file: str) -> None:
    index = get_pinecone_index() if index_name is None else get_pinecone_index(index_name)
    try:
        index.delete(filter={"source_file": {"$eq": source_file}}, namespace=collection)
    except Exception as exc:
        print(f"  delete source skipped ({exc})")


def purge_namespace(index_name: str | None, *, collection: str) -> None:
    index = get_pinecone_index() if index_name is None else get_pinecone_index(index_name)
    try:
        index.delete(delete_all=True, namespace=collection)
        print(f"  purged namespace {collection}")
    except Exception as exc:
        print(f"  purge skipped ({exc})")


def upsert_chunks(
    chunks: list[Chunk],
    vectors: list[list[float]],
    *,
    collection: str,
    index_name: str | None = None,
) -> int:
    assert len(chunks) == len(vectors), "chunks/vectors length mismatch"
    index = get_pinecone_index() if index_name is None else get_pinecone_index(index_name)

    items = []
    for c, v in zip(chunks, vectors):
        meta = c.meta.as_pinecone_metadata()
        meta[PINECONE_TEXT_FIELD] = _truncate_text_for_meta(c.text)
        items.append({"id": c.meta.chunk_id, "values": v, "metadata": meta})

    total = 0
    for i in range(0, len(items), PINECONE_BATCH):
        batch = items[i : i + PINECONE_BATCH]
        index.upsert(vectors=batch, namespace=collection)
        total += len(batch)
    return total


def write_parents_jsonl(parents: list[Parent], *, collection: str, append: bool = True) -> Path:
    out_dir = Path(PARENTS_PATH)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{collection}.jsonl"

    existing: dict[str, dict] = {}
    if append and path.exists():
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                existing[row["parent_id"]] = row

    for p in parents:
        existing[p.parent_id] = {
            "parent_id": p.parent_id,
            "collection": p.collection,
            "source_file": p.source_file,
            "section_path": p.section_path,
            "text": p.text,
        }

    with path.open("w", encoding="utf-8") as fh:
        for row in existing.values():
            fh.write(json.dumps(row, ensure_ascii=False))
            fh.write("\n")
    return path


def remove_parents_for_source(*, collection: str, source_file: str) -> int:
    path = Path(PARENTS_PATH) / f"{collection}.jsonl"
    if not path.exists():
        return 0
    rows = []
    removed = 0
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("source_file") == source_file:
                removed += 1
                continue
            rows.append(row)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False))
            fh.write("\n")
    return removed
