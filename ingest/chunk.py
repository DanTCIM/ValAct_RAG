from __future__ import annotations

import hashlib
from dataclasses import dataclass

import tiktoken
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from valact.metadata import ChunkMeta, chunk_id_for
from valact.settings import (
    CHUNK_OVERLAP_TOKENS,
    CHUNK_SIZE_TOKENS,
    HEADER_SUBSPLIT_THRESHOLD,
)

_ENC = tiktoken.get_encoding("cl100k_base")


def token_len(text: str) -> int:
    return len(_ENC.encode(text, disallowed_special=()))


_HEADER_SPLITTER = MarkdownHeaderTextSplitter(
    headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")],
    strip_headers=False,
)


def _section_path(meta: dict) -> str:
    parts = [meta.get(k, "") for k in ("h1", "h2", "h3")]
    return " > ".join(p for p in parts if p)


@dataclass
class Chunk:
    text: str
    meta: ChunkMeta


@dataclass
class Parent:
    parent_id: str
    collection: str
    source_file: str
    section_path: str
    text: str


def split_markdown(
    md_text: str,
    *,
    collection: str,
    source_file: str,
    chunk_size_tokens: int = CHUNK_SIZE_TOKENS,
    chunk_overlap_tokens: int = CHUNK_OVERLAP_TOKENS,
    subsplit_threshold: int = HEADER_SUBSPLIT_THRESHOLD,
) -> tuple[list[Chunk], list[Parent]]:
    blocks = _HEADER_SPLITTER.split_text(md_text)

    sub_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size_tokens,
        chunk_overlap=chunk_overlap_tokens,
        length_function=token_len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks: list[Chunk] = []
    parents: list[Parent] = []
    idx = 0
    for block_idx, block in enumerate(blocks):
        text = (block.page_content or "").strip()
        if not text:
            continue
        section_path = _section_path(block.metadata or {}) or "(root)"
        parent_key = f"{collection}|{source_file}|{block_idx}|{section_path}"
        parent_id = hashlib.sha1(parent_key.encode("utf-8")).hexdigest()[:16]
        parents.append(
            Parent(
                parent_id=parent_id,
                collection=collection,
                source_file=source_file,
                section_path=section_path,
                text=text,
            )
        )

        tlen = token_len(text)
        if tlen <= subsplit_threshold:
            pieces = [text]
        else:
            pieces = sub_splitter.split_text(text)

        for piece in pieces:
            piece = piece.strip()
            if not piece:
                continue
            cid = chunk_id_for(source_file, idx)
            idx += 1
            chunks.append(
                Chunk(
                    text=piece,
                    meta=ChunkMeta(
                        collection=collection,
                        source_file=source_file,
                        section_path=section_path,
                        chunk_id=cid,
                        parent_id=parent_id,
                        char_len=len(piece),
                        token_len=token_len(piece),
                    ),
                )
            )
    return chunks, parents
