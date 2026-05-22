from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable

import pandas as pd
import streamlit as st

from valact.settings import (
    BASE_MD_PATH,
    COLLECTIONS,
    DOCUMENT_LINK_PATH,
    DOCUMENT_LIST_PATH,
    SUMMARY_PATH,
)


@st.cache_data(show_spinner=False)
def _load_json(path: str, mtime: float) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _mtime(path: str) -> float:
    try:
        return os.path.getmtime(path)
    except OSError:
        return 0.0


def get_document_list() -> dict:
    return _load_json(DOCUMENT_LIST_PATH, _mtime(DOCUMENT_LIST_PATH))


def get_document_link() -> dict:
    return _load_json(DOCUMENT_LINK_PATH, _mtime(DOCUMENT_LINK_PATH))


def get_summary_data() -> dict:
    return _load_json(SUMMARY_PATH, _mtime(SUMMARY_PATH))


@st.cache_data(show_spinner=False)
def load_md(path: str, mtime: float) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def md_path_for(collection: str, document: str) -> Path:
    stem, _ = os.path.splitext(document)
    return Path(BASE_MD_PATH) / collection / f"{stem}.md"


def render_header(tab):
    with tab:
        st.header(
            "Life Actuarial Document Q&A Machine using Retrieval Augmented Generation (RAG)"
        )
        st.write(
            "Please see the sidebar to select a collection of documents. "
            "You can choose a specific document for an exclusive search within that document only."
        )


def render_disclaimer(model_name: str):
    with st.sidebar.expander("**Show me the evidence, AI**"):
        st.write(
            f"The *{model_name}*-powered RAG process searches actuarial documents. "
            "Harness its power **with accountability and responsibility**."
        )
        st.write("**AI responses should not be relied on as accurate or error-free.**")
        st.write(
            "Evaluate for accuracy. Read source documents. Review retrieved contexts. "
            "This is for educational use only."
        )


def render_doc_selector() -> tuple[str, str, str]:
    document_list = get_document_list()
    document_link = get_document_link()
    with st.sidebar:
        collection = st.selectbox("Select your document collection", COLLECTIONS)
        document = st.selectbox("Select your document", document_list[collection])
        link = document_link.get(document, "")
    return collection, document, link


def render_rag_params() -> tuple[int, bool, float]:
    with st.sidebar.expander("⚙️ RAG Parameters"):
        num_source = st.slider("Top N sources to view:", 4, 12, 6, 1)
        use_mmr = st.toggle(
            "Diversity search (MMR)",
            value=True,
            help="Reduces redundancy among retrieved candidates before reranking.",
        )
        lambda_mult = st.slider("Diversity parameter (lambda):", 0.0, 1.0, 0.5, 0.25)
    return num_source, use_mmr, lambda_mult


def render_summary(document: str):
    if document == "All":
        return
    summary = get_summary_data().get(document)
    with st.sidebar.expander("AI generated summary of the document", expanded=True):
        if summary:
            st.write(summary.get("summary", "Summary not available."))
        else:
            st.write(f"Summary of '{document}' not found.")


def render_doc_link(document: str, link: str):
    if document != "All":
        with st.sidebar.container(border=True):
            st.write(f"**View Source** (tab TXT-doc or link below): {link}")


def render_md_viewer(tab, collection: str, document: str):
    if document == "All":
        with tab:
            st.write(
                "When you select a document, this tab shows the pre-converted Markdown content. "
                "Use the source link in the sidebar for canonical viewing."
            )
        return
    path = md_path_for(collection, document)
    with tab:
        with st.container(height=700):
            if path.exists():
                st.write(load_md(str(path), _mtime(str(path))), unsafe_allow_html=True)
            else:
                st.write(f"Markdown not found at {path}")


def render_chat_history(tab, messages: Iterable[dict]):
    with tab:
        for msg in messages:
            role = msg.get("role")
            if role not in ("user", "assistant"):
                continue
            content = msg.get("content", "")
            kind = msg.get("kind")
            if kind == "sources":
                query = msg.get("query", "")
                with st.expander(f"📖 **Context Retrieval:** {query}", expanded=False):
                    st.markdown(content, unsafe_allow_html=True)
            else:
                st.chat_message(role).write(content)


def format_sources_block(parents, num_source: int) -> str:
    parts = []
    for i, p in enumerate(parents[:num_source], start=1):
        score = (
            f"\n* **Relevance: {round((p.best_rerank_score or 0) * 100)}%**"
            if p.best_rerank_score is not None
            else ""
        )
        parts.append(
            f"### Retrieval {i}\n"
            f"* **Document: {p.source_file}**\n"
            f"* **Section: {p.section_path}**{score}\n\n"
            f"{p.text}\n"
        )
    return "\n\n".join(parts)


def render_sources_now(container, parents, num_source: int):
    status = container.status("**Context Retrieval**", expanded=False)
    status.markdown(format_sources_block(parents, num_source), unsafe_allow_html=True)
    status.update(state="complete")


def render_sidebar_buttons(messages: list[dict], on_clear):
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                "Clear history",
                use_container_width=True,
                on_click=on_clear,
                help="Clear history to start fresh.",
            )
        with col2:
            df = pd.DataFrame(
                [
                    {"role": m.get("role"), "kind": m.get("kind", ""), "content": m.get("content", "")}
                    for m in messages
                ]
            )
            st.download_button(
                "Download history",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="chat_history.csv",
                mime="text/csv",
                use_container_width=True,
            )
        st.caption(
            "🖋️ Project code at [GitHub](https://github.com/DanTCIM/ValAct_RAG)."
        )
