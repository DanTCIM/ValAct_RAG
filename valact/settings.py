from __future__ import annotations

import os
from dataclasses import dataclass

try:
    import streamlit as st

    _HAS_STREAMLIT = True
except ImportError:
    _HAS_STREAMLIT = False


def _secret(name: str, default: str | None = None) -> str | None:
    if _HAS_STREAMLIT:
        try:
            return st.secrets[name]
        except (KeyError, FileNotFoundError, AttributeError):
            pass
    return os.environ.get(name, default)


PINECONE_INDEX = "valact-rag-v3"
PINECONE_INDEX_LEGACY = "valact-rag"

EMBED_PROVIDER = "voyage"  # "voyage" or "openai"
EMBED_MODEL = "voyage-finance-2"
EMBED_DIM = 1024

# Single source of truth for the chat LLM. Used by the main RAG answer pipeline
# (valact.rag.answer_stream) and the FRED/JGB tool-use chat (valact.yield_chat).
# Change this in one place to update everywhere.
ANTHROPIC_MODEL = "claude-sonnet-4-6"

COHERE_RERANK_MODEL = "rerank-v3.5"

RETRIEVE_TOP_K = 40
RERANK_TOP_N = 10
MAX_CONTEXT_PARENTS = 8
MMR_LAMBDA_DEFAULT = 0.5

CHUNK_SIZE_TOKENS = 800
CHUNK_OVERLAP_TOKENS = 100
HEADER_SUBSPLIT_THRESHOLD = 1200

USE_RERANK = True
RERANK_TIMEOUT_S = 2.0

COLLECTIONS = [
    "SAP",
    "PBR",
    "CFT",
    "ASOP_life",
    "GAAP",
    "IFRS17",
    "Bermuda",
    "Cayman",
    "Asset",
    "Product",
    "RiskFinance",
    "AI_BigData",
]

COLLECTION_LABELS = {
    "SAP": "Statutory Accounting Principles (SAP)",
    "PBR": "PBR",
    "CFT": "CFT",
    "ASOP_life": "ASOP_life",
    "GAAP": "GAAP",
    "IFRS17": "IFRS17",
    "Bermuda": "Bermuda",
    "Cayman": "Cayman",
    "Asset": "Asset",
    "Product": "Product",
    "RiskFinance": "RiskFinance (Risk and finance including capital, reinsurance topics)",
    "AI_BigData": "AI_BigData",
}

BASE_PDF_PATH = "./data/pdf"
BASE_MD_PATH = "./data/md"
PARENTS_PATH = "./data/parents"
SUMMARY_PATH = "./data/summary.json"
DOCUMENT_LIST_PATH = "./data/document_list.json"
DOCUMENT_LINK_PATH = "./data/document_link.json"


@dataclass(frozen=True)
class Secrets:
    openai: str
    anthropic: str
    pinecone: str
    cohere: str | None
    voyage: str | None


def get_secrets() -> Secrets:
    return Secrets(
        openai=_secret("OPENAI_API_KEY") or "",
        anthropic=_secret("ANTHROPIC_API_KEY") or "",
        pinecone=_secret("PINECONE_API_KEY") or "",
        cohere=_secret("COHERE_API_KEY"),
        voyage=_secret("VOYAGE_API_KEY"),
    )
