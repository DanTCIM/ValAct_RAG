from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from anthropic import Anthropic
from openai import OpenAI
from pinecone import Pinecone

from valact.settings import (
    BASE_MD_PATH,
    PARENTS_PATH,
    PINECONE_INDEX,
    Secrets,
    get_secrets,
)

try:
    import cohere

    _HAS_COHERE = True
except ImportError:
    _HAS_COHERE = False

try:
    import voyageai

    _HAS_VOYAGE = True
except ImportError:
    _HAS_VOYAGE = False

try:
    import streamlit as st

    _cache_resource = st.cache_resource
except ImportError:

    def _cache_resource(func=None, **_kwargs):
        if func is None:
            return lambda f: lru_cache(maxsize=1)(f)
        return lru_cache(maxsize=1)(func)


@_cache_resource(show_spinner=False)
def _secrets() -> Secrets:
    return get_secrets()


@_cache_resource(show_spinner=False)
def get_openai_client() -> OpenAI:
    return OpenAI(api_key=_secrets().openai)


@_cache_resource(show_spinner=False)
def get_anthropic_client() -> Anthropic:
    return Anthropic(api_key=_secrets().anthropic)


@_cache_resource(show_spinner=False)
def get_pinecone_client() -> Pinecone:
    return Pinecone(api_key=_secrets().pinecone)


@_cache_resource(show_spinner=False)
def get_pinecone_index(index_name: str = PINECONE_INDEX):
    return get_pinecone_client().Index(index_name)


@_cache_resource(show_spinner=False)
def get_cohere_client():
    if not _HAS_COHERE:
        return None
    key = _secrets().cohere
    if not key:
        return None
    return cohere.ClientV2(api_key=key)


@_cache_resource(show_spinner=False)
def get_voyage_client():
    if not _HAS_VOYAGE:
        return None
    key = _secrets().voyage
    if not key:
        return None
    return voyageai.Client(api_key=key)


def _regenerate_parents_jsonl(collection: str, path: Path) -> None:
    # Local import to avoid load-time cycles; ingest depends on valact.* too.
    from ingest.chunk import split_markdown

    md_dir = Path(BASE_MD_PATH) / collection
    if not md_dir.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    rows: dict[str, dict[str, Any]] = {}
    for md_path in sorted(md_dir.glob("*.md")):
        source_file = md_path.stem + ".pdf"
        md_text = md_path.read_text(encoding="utf-8")
        _, parents = split_markdown(md_text, collection=collection, source_file=source_file)
        for p in parents:
            rows[p.parent_id] = {
                "parent_id": p.parent_id,
                "collection": p.collection,
                "source_file": p.source_file,
                "section_path": p.section_path,
                "text": p.text,
            }
    with path.open("w", encoding="utf-8") as fh:
        for row in rows.values():
            fh.write(json.dumps(row, ensure_ascii=False))
            fh.write("\n")


@_cache_resource(show_spinner=False)
def get_parents(collection: str) -> dict[str, dict[str, Any]]:
    path = Path(PARENTS_PATH) / f"{collection}.jsonl"
    if not path.exists():
        _regenerate_parents_jsonl(collection, path)
    out: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return out
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            out[row["parent_id"]] = row
    return out
