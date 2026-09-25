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
ANTHROPIC_MODEL = "claude-sonnet-5"

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

# Sidebar option that turns on Jev-assisted domain routing instead of a single
# hand-picked collection. Deliberately NOT part of COLLECTIONS -- the ingest
# pipeline (ingest/classify.py, ingest/add_doc.py) iterates that list as the
# real taxonomy.
AUTO_OPTION = "Auto"

# Jev (TypeSafe System One) via OpenRouter's Decisions API. This is NOT a chat
# model: it takes a `state` plus typed questions and returns calibrated
# probabilities, so chat-completions SDKs do not work against it.
JEV_ENDPOINT = "https://openrouter.ai/api/alpha/decisions"
JEV_MODEL = "~typesafe/jev-latest"  # alias -> typesafe/jev-1.13; pin if results drift
JEV_TIMEOUT_S = 5.0

# Domain picker behavior in Auto mode.
# Pre-check domains at/above this probability (the top one is always checked).
# Tuned on scripts/eval_router.py over 25 labeled queries: 0.7 still pre-checks
# the labeled domain 25/25 while averaging 1.7 domains instead of 2.9 at 0.5.
AUTO_PRECHECK_THRESHOLD = 0.7
AUTO_TOP_VISIBLE = 5  # remaining domains go under an expander

# Below this P(on-topic) the Auto picker warns and pre-checks nothing, so an
# off-topic question costs no retrieval or answer call unless the user insists.
# Tuned on scripts/eval_gates.py.
AUTO_OFFTOPIC_THRESHOLD = 0.3

# Follow-up detection (both modes, only when a previous question exists). At or
# above this P(follow-up), routing and retrieval search on the previous
# question(s) joined with the new one. Tuned on scripts/eval_gates.py.
FOLLOWUP_THRESHOLD = 0.5
MAX_CONTEXT_QUESTIONS = 3  # cap on questions chained into one search query

# Short display names, shown in the Auto picker and used as the taxonomy
# catalog when ingest/classify.py files a new document.
COLLECTION_LABELS = {
    "SAP": "Statutory accounting & NAIC valuation",
    "PBR": "Principle-based reserving (Valuation Manual)",
    "CFT": "Cash flow testing & asset adequacy",
    "ASOP_life": "Actuarial Standards of Practice",
    "GAAP": "US GAAP (LDTI)",
    "IFRS17": "IFRS 17",
    "Bermuda": "Bermuda (BMA)",
    "Cayman": "Cayman (CIMA)",
    "Asset": "Investment assets",
    "Product": "Product pricing & experience studies",
    "RiskFinance": "Risk, capital & reinsurance finance",
    "AI_BigData": "AI & big data in insurance",
}

# Topic descriptions used as Jev question instructions when routing a question
# to collections. Jev reads instructions literally, so these are deliberately
# keyword-heavy (the short COLLECTION_LABELS above are far too thin to route on).
COLLECTION_DESCRIPTIONS = {
    "SAP": (
        "US statutory accounting and NAIC valuation requirements for life insurers: SSAPs, "
        "Standard Valuation Law, actuarial guidelines AG 33, AG 35, AG 38, AG 48 XXX/AXXX "
        "captives, AVR and IMR including negative IMR and INT 23-01, risk-based capital (RBC, "
        "C3 Phase 1 and Phase 2), and the principles-based bond definition."
    ),
    "PBR": (
        "US principles-based reserving under the NAIC Valuation Manual: VM-20 life reserves, "
        "VM-21 variable annuities, VM-22 non-variable annuities, VM-30, VM-31 PBR reports, "
        "VM-50/VM-51 experience reporting, deterministic and stochastic reserves, net premium "
        "reserve, the GOES economic scenario generator, PBR assumptions, credibility, and "
        "PBR model governance."
    ),
    "CFT": (
        "Cash flow testing and asset adequacy analysis: the actuarial opinion and memorandum, "
        "NAIC Model Regulation 822, New York Regulation 126 scenarios, AG 53 for complex assets "
        "and spreads, AG 55, ASOP 22 opinions, and the Academy interest rate generator (AIRG)."
    ),
    "ASOP_life": (
        "US Actuarial Standards of Practice issued by the Actuarial Standards Board: the numbered "
        "ASOPs covering data quality, credibility, modeling, actuarial communications, risk "
        "classification, reinsurance, nonguaranteed elements, illustrations, pricing, capital "
        "adequacy, ERM, and statements of actuarial opinion. Questions about professional "
        "standards and what an ASOP requires."
    ),
    "GAAP": (
        "US GAAP accounting for long-duration insurance contracts: FASB ASU 2018-12 (LDTI), "
        "liability for future policy benefits, market risk benefits (MRB), deferred acquisition "
        "costs, embedded derivatives (DIG B36, modified coinsurance), purchase GAAP, reinsured "
        "business, and non-GAAP earnings measures."
    ),
    "IFRS17": (
        "IFRS 17 Insurance Contracts: general measurement model, premium allocation approach, "
        "variable fee approach, contractual service margin, risk adjustment, transition, "
        "reinsurance held, IFRS 17 implementation, and IFRS 18 presentation for insurers."
    ),
    "Bermuda": (
        "Bermuda Monetary Authority (BMA) regulation of long-term insurers and reinsurers: "
        "Economic Balance Sheet (EBS), BSCR capital, the scenario-based approach (SBA, LLSBA), "
        "prudent person principle, BMA stress testing and GFC scenarios, liquidity risk, "
        "asset-intensive reinsurance, public disclosure, group supervision, recovery planning, "
        "and the Bermuda Corporate Income Tax Act."
    ),
    "Cayman": (
        "Cayman Islands Monetary Authority (CIMA) insurance regulation: licensing of Class B, "
        "Class C and Class D insurers, actuarial valuation rules, recognition and approval of "
        "the appointed actuary, investment activities rules, reinsurance arrangements, and risk "
        "management rules for Cayman insurers."
    ),
    "Asset": (
        "Insurer investment assets and NAIC asset primers: private credit and direct loans, CLOs "
        "and combo notes, consumer and auto ABS, commercial mortgage loans, commercial real "
        "estate, leveraged bank loans, derivatives, hedge funds, securities lending, Federal Home "
        "Loan Bank funding, funding agreement backed notes, complex assets, and investment "
        "modeling guidance."
    ),
    "Product": (
        "Life and annuity product pricing, design and experience studies: mortality tables and "
        "mortality improvement, lapse, surrender and premium persistency, policyholder behavior, "
        "credibility methods and experience study calculations, term conversion, policyholder "
        "dividends and nonguaranteed elements, AG 49-A illustrations, long-term care pricing, "
        "structured settlements, pension risk transfer, payout annuity mortality, and VA/RILA "
        "behavior studies."
    ),
    "RiskFinance": (
        "Insurance risk management and finance: economic capital, regulatory and group capital, "
        "IAIS ICS, rating agency capital models, ORSA and ERM, operational risk, model risk "
        "management and model validation, liquidity risk, reinsurance structures including "
        "coinsurance, funds withheld, reserve credit and asset-intensive reinsurance, embedded "
        "value, insurance tax, economic scenario generators, real-world versus risk-neutral "
        "scenarios, and nested stochastic modeling."
    ),
    "AI_BigData": (
        "Artificial intelligence, machine learning and big data in insurance: predictive "
        "analytics, generative AI, AI governance and ethics, the NAIC AI model bulletin and AI "
        "principles, Colorado AI regulation, data bias and algorithmic fairness, correlation "
        "versus causation, and supervisory expectations for insurers' use of AI."
    ),
}

BASE_PDF_PATH = "./data/pdf"
BASE_MD_PATH = "./data/md"
PARENTS_PATH = "./data/parents"
SUMMARY_PATH = "./data/summary.json"
DOCUMENT_LIST_PATH = "./data/document_list.json"
DOCUMENT_LINK_PATH = "./data/document_link.json"
INBOX_PATH = "./data/inbox"
INBOX_MANIFEST_PATH = "./data/inbox/manifest.csv"
ADD_DOC_STATE_PATH = "./.add_doc_state"


@dataclass(frozen=True)
class Secrets:
    openai: str
    anthropic: str
    pinecone: str
    cohere: str | None
    voyage: str | None
    mathpix_app_id: str | None
    mathpix_app_key: str | None
    openrouter_valact: str | None


def get_secrets() -> Secrets:
    return Secrets(
        openai=_secret("OPENAI_API_KEY") or "",
        anthropic=_secret("ANTHROPIC_API_KEY") or "",
        pinecone=_secret("PINECONE_API_KEY") or "",
        cohere=_secret("COHERE_API_KEY"),
        voyage=_secret("VOYAGE_API_KEY"),
        mathpix_app_id=_secret("MATHPIX_APP_ID"),
        mathpix_app_key=_secret("MATHPIX_APP_KEY") or _secret("MATHPIX_API_KEY"),
        openrouter_valact=_secret("OPENROUTER_VALACT_KEY"),
    )
