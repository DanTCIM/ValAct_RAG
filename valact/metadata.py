from __future__ import annotations

import re
from dataclasses import asdict, dataclass


@dataclass
class ChunkMeta:
    collection: str
    source_file: str
    section_path: str
    chunk_id: str
    parent_id: str
    char_len: int
    token_len: int

    def as_pinecone_metadata(self) -> dict:
        return asdict(self)


def chunk_id_for(source_file: str, idx: int) -> str:
    return f"{source_file}::{idx:04d}"


_SAFE_ID = re.compile(r"[^A-Za-z0-9_.:-]+")


def safe_id(value: str) -> str:
    return _SAFE_ID.sub("_", value)
