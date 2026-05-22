from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from pinecone import ServerlessSpec

from valact.clients import get_pinecone_client
from valact.settings import (
    BASE_MD_PATH,
    COLLECTIONS,
    EMBED_DIM,
    PINECONE_INDEX,
)

from ingest.chunk import split_markdown
from ingest.embed import embed_iter
from ingest.upsert import (
    delete_source,
    purge_namespace,
    remove_parents_for_source,
    upsert_chunks,
    write_parents_jsonl,
)


def ensure_index(name: str = PINECONE_INDEX, dim: int = EMBED_DIM) -> None:
    pc = get_pinecone_client()
    existing = {idx["name"] for idx in pc.list_indexes()}
    if name in existing:
        return
    print(f"Creating Pinecone index {name} (dim={dim}, metric=cosine)...")
    pc.create_index(
        name=name,
        dimension=dim,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while True:
        desc = pc.describe_index(name)
        ready = desc["status"]["ready"] if isinstance(desc, dict) else desc.status.get("ready")
        if ready:
            break
        time.sleep(2)
    print(f"  index {name} ready")


def ingest_file(md_path: Path, *, collection: str, index_name: str, purged: bool) -> tuple[int, int]:
    source_file = md_path.stem + ".pdf"
    md_text = md_path.read_text(encoding="utf-8")
    chunks, parents = split_markdown(md_text, collection=collection, source_file=source_file)
    if not chunks:
        print(f"  {source_file}: no chunks, skipping")
        return 0, 0

    if not purged:
        delete_source(index_name, collection=collection, source_file=source_file)
        remove_parents_for_source(collection=collection, source_file=source_file)

    print(f"  embedding {len(chunks)} chunks for {source_file}...")
    vectors = embed_iter([c.text for c in chunks])
    n_up = upsert_chunks(chunks, vectors, collection=collection, index_name=index_name)
    write_parents_jsonl(parents, collection=collection, append=True)
    return n_up, len(parents)


def ingest_collection(
    collection: str,
    *,
    index_name: str,
    purge: bool,
    only_file: str | None = None,
) -> None:
    md_dir = Path(BASE_MD_PATH) / collection
    if not md_dir.exists():
        print(f"[{collection}] no MD directory at {md_dir}; skipping")
        return

    md_files = sorted(md_dir.glob("*.md"))
    if only_file:
        md_files = [p for p in md_files if p.name == only_file or p.stem + ".pdf" == only_file]
        if not md_files:
            print(f"[{collection}] no MD matching {only_file}")
            return

    print(f"[{collection}] {len(md_files)} files")
    if purge:
        purge_namespace(index_name, collection=collection)
        parents_path = Path("./data/parents") / f"{collection}.jsonl"
        if parents_path.exists():
            parents_path.unlink()

    total_chunks = 0
    total_parents = 0
    t0 = time.perf_counter()
    for md_path in md_files:
        n_chunks, n_parents = ingest_file(
            md_path, collection=collection, index_name=index_name, purged=purge
        )
        total_chunks += n_chunks
        total_parents += n_parents
    print(
        f"[{collection}] done: {total_chunks} chunks, {total_parents} parents "
        f"in {time.perf_counter() - t0:.1f}s"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--collection", help="Collection to ingest (e.g. SAP)")
    ap.add_argument("--file", help="Specific filename to (re)ingest")
    ap.add_argument("--all", action="store_true", help="Ingest all collections")
    ap.add_argument("--purge", action="store_true", help="Delete namespace + parents before ingest")
    ap.add_argument("--index", default=PINECONE_INDEX)
    args = ap.parse_args()

    if not args.all and not args.collection:
        ap.error("--collection or --all required")

    ensure_index(args.index)

    if args.all:
        collections = COLLECTIONS
    else:
        collections = [args.collection]

    for c in collections:
        ingest_collection(c, index_name=args.index, purge=args.purge, only_file=args.file)


if __name__ == "__main__":
    main()
