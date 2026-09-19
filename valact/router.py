"""Route a question to document collections with Jev (TypeSafe System One).

Jev is a decision model, not a chat model: it takes a `state` plus typed
questions and returns calibrated probabilities. It is reached through
OpenRouter's Decisions API (`POST /api/alpha/decisions`), which is separate
from `/api/v1/chat/completions` -- chat SDKs do not work against it.

One `noul` (yes/no probability) question per collection goes out in a single
request, so each collection gets an independent relevance probability and a
question that spans two domains can score high on both. Every failure path
returns None; the caller falls back to an unranked manual pick.
"""

from __future__ import annotations

import json

import httpx

from valact.settings import (
    COLLECTION_DESCRIPTIONS,
    COLLECTIONS,
    JEV_ENDPOINT,
    JEV_MODEL,
    JEV_TIMEOUT_S,
    get_secrets,
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


_QUESTION_TEMPLATE = (
    "Would documents on the following topic help answer the user's question? "
    "Topic: {description}"
)


def _questions() -> dict[str, dict]:
    return {
        collection: {
            "type": "noul",
            "instructions": _QUESTION_TEMPLATE.format(
                description=COLLECTION_DESCRIPTIONS.get(collection, collection)
            ),
        }
        for collection in COLLECTIONS
    }


def _rank_impl(query: str) -> list[tuple[str, float]] | None:
    key = get_secrets().openrouter_valact
    if not key or not query.strip():
        return None

    payload = {
        "model": JEV_MODEL,
        "state": {"user_question": query},
        "questions": _questions(),
    }
    try:
        resp = httpx.post(
            JEV_ENDPOINT,
            json=payload,
            headers={"Authorization": f"Bearer {key}"},
            timeout=JEV_TIMEOUT_S,
        )
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, json.JSONDecodeError, ValueError):
        return None

    answers = data.get("answers")
    if not isinstance(answers, dict):
        return None

    ranking: list[tuple[str, float]] = []
    for collection in COLLECTIONS:
        answer = answers.get(collection)
        if not isinstance(answer, dict) or "noul" not in answer:
            continue
        try:
            ranking.append((collection, float(answer["noul"])))
        except (TypeError, ValueError):
            continue

    if not ranking:
        return None
    ranking.sort(key=lambda pair: pair[1], reverse=True)
    return ranking


@_cache_data(ttl=3600, show_spinner=False)
def rank_collections(query: str) -> list[tuple[str, float]] | None:
    """Collections ordered by P(relevant), or None if Jev is unavailable."""
    return _rank_impl(query)
