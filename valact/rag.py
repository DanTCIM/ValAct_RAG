from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Iterator

import numpy as np

from valact.clients import (
    get_anthropic_client,
    get_cohere_client,
    get_parents,
    get_pinecone_index,
)
from valact.embed import embed_query
from valact.settings import (
    ANTHROPIC_MODEL,
    COHERE_RERANK_MODEL,
    MAX_CONTEXT_PARENTS,
    MMR_LAMBDA_DEFAULT,
    RERANK_TIMEOUT_S,
    RERANK_TOP_N,
    RETRIEVE_TOP_K,
    USE_RERANK,
)

try:
    import streamlit as st

    _cache_data = st.cache_data
except ImportError:

    def _cache_data(*_args, **_kwargs):
        def _decorator(func):
            return func

        if _args and callable(_args[0]):
            return _args[0]
        return _decorator


@dataclass
class Doc:
    chunk_id: str
    text: str
    source_file: str
    section_path: str
    collection: str
    parent_id: str
    score: float = 0.0
    rerank_score: float | None = None
    embedding: list[float] | None = field(default=None, repr=False)


@dataclass
class ParentDoc:
    parent_id: str
    source_file: str
    section_path: str
    collection: str
    text: str
    children: list[Doc] = field(default_factory=list)
    best_rerank_score: float | None = None


def _pinecone_filter(document: str | None) -> dict | None:
    if not document or document == "All":
        return None
    return {"source_file": {"$eq": document}}


def _docs_from_matches(matches, collection: str) -> list[Doc]:
    docs: list[Doc] = []
    for m in matches:
        md = m.get("metadata", {}) if isinstance(m, dict) else dict(m.metadata or {})
        score = m.get("score", 0.0) if isinstance(m, dict) else float(m.score)
        values = m.get("values") if isinstance(m, dict) else getattr(m, "values", None)
        docs.append(
            Doc(
                chunk_id=md.get("chunk_id") or (m.get("id") if isinstance(m, dict) else m.id),
                text=md.get("text", ""),
                source_file=md.get("source_file", ""),
                section_path=md.get("section_path", ""),
                collection=md.get("collection", collection),
                parent_id=md.get("parent_id", ""),
                score=score,
                embedding=list(values) if values else None,
            )
        )
    return docs


def _mmr(query_vec: list[float], docs: list[Doc], k: int, lambda_mult: float) -> list[Doc]:
    if not docs:
        return docs
    qv = np.array(query_vec, dtype=np.float32)
    qv /= np.linalg.norm(qv) + 1e-9

    vecs = []
    for d in docs:
        if d.embedding is None:
            return docs[:k]
        v = np.array(d.embedding, dtype=np.float32)
        v /= np.linalg.norm(v) + 1e-9
        vecs.append(v)
    vecs_arr = np.stack(vecs)
    sim_to_query = vecs_arr @ qv

    selected: list[int] = []
    remaining = set(range(len(docs)))
    while remaining and len(selected) < k:
        if not selected:
            i = int(np.argmax(sim_to_query))
            selected.append(i)
            remaining.discard(i)
            continue
        selected_vecs = vecs_arr[selected]
        scores = {}
        for i in remaining:
            redundancy = float(np.max(selected_vecs @ vecs_arr[i]))
            scores[i] = lambda_mult * float(sim_to_query[i]) - (1 - lambda_mult) * redundancy
        i = max(scores, key=scores.get)
        selected.append(i)
        remaining.discard(i)
    return [docs[i] for i in selected]


def _retrieve_impl(
    query: str,
    *,
    collection: str,
    document: str | None,
    top_k: int,
    use_mmr: bool,
    lambda_mult: float,
) -> list[Doc]:
    index = get_pinecone_index()
    qv = embed_query(query)

    fetch_k = int(top_k * 1.5) if use_mmr else top_k
    resp = index.query(
        vector=qv,
        top_k=fetch_k,
        namespace=collection,
        include_metadata=True,
        include_values=use_mmr,
        filter=_pinecone_filter(document),
    )
    matches = resp.get("matches", []) if isinstance(resp, dict) else resp.matches
    docs = _docs_from_matches(matches, collection)
    if use_mmr:
        docs = _mmr(qv, docs, k=top_k, lambda_mult=lambda_mult)
    return docs


@_cache_data(ttl=3600, show_spinner=False)
def retrieve(
    query: str,
    *,
    collection: str,
    document: str | None = None,
    top_k: int = RETRIEVE_TOP_K,
    use_mmr: bool = True,
    lambda_mult: float = MMR_LAMBDA_DEFAULT,
) -> list[Doc]:
    return _retrieve_impl(
        query,
        collection=collection,
        document=document,
        top_k=top_k,
        use_mmr=use_mmr,
        lambda_mult=lambda_mult,
    )


def _rerank_impl(query: str, docs: list[Doc], top_n: int) -> list[Doc]:
    if not docs or not USE_RERANK:
        return docs[:top_n]
    client = get_cohere_client()
    if client is None:
        return docs[:top_n]
    try:
        resp = client.rerank(
            model=COHERE_RERANK_MODEL,
            query=query,
            documents=[d.text for d in docs],
            top_n=min(top_n, len(docs)),
            request_options={"timeout": RERANK_TIMEOUT_S},
        )
    except Exception:
        return docs[:top_n]

    out: list[Doc] = []
    for r in resp.results:
        d = docs[r.index]
        d.rerank_score = float(r.relevance_score)
        out.append(d)
    return out


@_cache_data(ttl=3600, show_spinner=False)
def rerank(query: str, docs: list[Doc], top_n: int = RERANK_TOP_N) -> list[Doc]:
    return _rerank_impl(query, docs, top_n)


def expand_parents(docs: list[Doc], *, max_parents: int = MAX_CONTEXT_PARENTS) -> list[ParentDoc]:
    by_parent: dict[str, ParentDoc] = {}
    order: list[str] = []
    for d in docs:
        if not d.parent_id:
            continue
        if d.parent_id not in by_parent:
            parents_map = get_parents(d.collection)
            p = parents_map.get(d.parent_id)
            if not p:
                continue
            by_parent[d.parent_id] = ParentDoc(
                parent_id=d.parent_id,
                source_file=p.get("source_file", d.source_file),
                section_path=p.get("section_path", d.section_path),
                collection=p.get("collection", d.collection),
                text=p.get("text", ""),
                best_rerank_score=d.rerank_score,
            )
            order.append(d.parent_id)
        by_parent[d.parent_id].children.append(d)
        cur = by_parent[d.parent_id].best_rerank_score
        if d.rerank_score is not None and (cur is None or d.rerank_score > cur):
            by_parent[d.parent_id].best_rerank_score = d.rerank_score

    parents = [by_parent[pid] for pid in order]
    return parents[:max_parents]


SYSTEM_PROMPT = (
    "You are an actuarial research assistant for life insurance valuation, accounting, "
    "and regulatory topics. Answer the user's question using ONLY the provided context. "
    "Cite sources inline as [source_file: section_path] after each claim that depends on the context. "
    "If the answer is not contained in the context, say so plainly and do not speculate. "
    "Prefer precise, technical language. Use bulleted lists for enumerable items."
)


def _format_context_block(parents: list[ParentDoc]) -> str:
    parts = []
    for i, p in enumerate(parents, start=1):
        header = f"[{i}] source_file: {p.source_file} | section_path: {p.section_path}"
        parts.append(f"{header}\n{p.text.strip()}")
    return "\n\n---\n\n".join(parts)


def build_messages(
    query: str,
    history: list[dict],
    parents: list[ParentDoc],
) -> tuple[list[dict], list[dict]]:
    context_block = _format_context_block(parents)
    system = [
        {"type": "text", "text": SYSTEM_PROMPT},
        {
            "type": "text",
            "text": f"<context>\n{context_block}\n</context>",
            "cache_control": {"type": "ephemeral"},
        },
    ]

    messages: list[dict] = []
    for turn in history[-4:]:
        role = turn.get("role")
        content = turn.get("content", "")
        if role in ("user", "assistant") and content:
            messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": query})
    return system, messages


def history_aware_query(query: str, history: list[dict]) -> str:
    last_user = None
    for turn in reversed(history):
        if turn.get("role") == "user":
            last_user = turn.get("content", "")
            break
    if not last_user:
        return query
    return f"{last_user}\n{query}"


def answer_stream(
    query: str,
    history: list[dict],
    parents: list[ParentDoc],
    *,
    max_tokens: int = 1024,
) -> Iterator[str]:
    client = get_anthropic_client()
    system, messages = build_messages(query, history, parents)
    with client.messages.stream(
        model=ANTHROPIC_MODEL,
        system=system,
        messages=messages,
        max_tokens=max_tokens,
    ) as stream:
        for chunk in stream.text_stream:
            yield chunk


@dataclass
class StageTimings:
    embed_s: float = 0.0
    pinecone_s: float = 0.0
    rerank_s: float = 0.0
    expand_s: float = 0.0
    total_s: float = 0.0


def run_retrieval(
    query: str,
    *,
    collection: str,
    document: str | None = None,
    top_k: int = RETRIEVE_TOP_K,
    top_n: int = RERANK_TOP_N,
    use_mmr: bool = True,
    lambda_mult: float = MMR_LAMBDA_DEFAULT,
    max_parents: int = MAX_CONTEXT_PARENTS,
    timings: StageTimings | None = None,
) -> tuple[list[Doc], list[ParentDoc]]:
    t0 = time.perf_counter()
    t = time.perf_counter()
    qv = embed_query(query)
    if timings:
        timings.embed_s = time.perf_counter() - t

    t = time.perf_counter()
    index = get_pinecone_index()
    fetch_k = int(top_k * 1.5) if use_mmr else top_k
    resp = index.query(
        vector=qv,
        top_k=fetch_k,
        namespace=collection,
        include_metadata=True,
        include_values=use_mmr,
        filter=_pinecone_filter(document),
    )
    matches = resp.get("matches", []) if isinstance(resp, dict) else resp.matches
    docs = _docs_from_matches(matches, collection)
    if use_mmr:
        docs = _mmr(qv, docs, k=top_k, lambda_mult=lambda_mult)
    if timings:
        timings.pinecone_s = time.perf_counter() - t

    t = time.perf_counter()
    docs = _rerank_impl(query, docs, top_n=top_n)
    if timings:
        timings.rerank_s = time.perf_counter() - t

    t = time.perf_counter()
    parents = expand_parents(docs, max_parents=max_parents)
    if timings:
        timings.expand_s = time.perf_counter() - t
        timings.total_s = time.perf_counter() - t0

    return docs, parents
