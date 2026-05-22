from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Actuarial Doc Q&A Model", page_icon="📖", layout="wide")

from valact.rag import answer_stream, expand_parents, rerank, retrieve
from valact.settings import ANTHROPIC_MODEL, MAX_CONTEXT_PARENTS, RERANK_TOP_N, RETRIEVE_TOP_K
from valact.ui import (
    format_sources_block,
    render_chat_history,
    render_disclaimer,
    render_doc_link,
    render_doc_selector,
    render_header,
    render_md_viewer,
    render_rag_params,
    render_sidebar_buttons,
    render_summary,
)


WELCOME = "Welcome to life actuarial document Q&A machine!"


def _init_history():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": WELCOME}]


def _clear_history():
    st.session_state.messages = [{"role": "assistant", "content": WELCOME}]


def _llm_only_history(messages: list[dict]) -> list[dict]:
    return [
        {"role": m["role"], "content": m["content"]}
        for m in messages
        if m.get("kind") != "sources" and m.get("role") in ("user", "assistant")
    ]


def main():
    _init_history()
    tab_qa, tab_md = st.tabs(["Q&A", "TXT-doc"])
    render_header(tab_qa)
    render_disclaimer(ANTHROPIC_MODEL)

    collection, document, doc_link = render_doc_selector()
    num_source, use_mmr, lambda_mult = render_rag_params()

    render_chat_history(tab_qa, st.session_state.messages)
    render_doc_link(document, doc_link)
    render_md_viewer(tab_md, collection, document)
    render_summary(document)

    if user_query := st.chat_input(
        placeholder="What is your question on the selected collection/document?"
    ):
        st.session_state.messages.append({"role": "user", "content": user_query})
        with tab_qa:
            st.chat_message("user").write(user_query)
            with st.chat_message("assistant"):
                sources_box = st.container()
                stream_box = st.empty()

                docs = retrieve(
                    user_query,
                    collection=collection,
                    document=None if document == "All" else document,
                    top_k=RETRIEVE_TOP_K,
                    use_mmr=use_mmr,
                    lambda_mult=lambda_mult,
                )
                reranked = rerank(user_query, docs, top_n=RERANK_TOP_N)
                parents = expand_parents(reranked, max_parents=MAX_CONTEXT_PARENTS)

                sources_md = format_sources_block(parents, num_source)
                status = sources_box.status("**Context Retrieval**", expanded=False)
                status.markdown(sources_md, unsafe_allow_html=True)
                status.update(state="complete")

                history = _llm_only_history(st.session_state.messages[:-1])

                text = ""
                try:
                    for chunk in answer_stream(user_query, history, parents):
                        text += chunk
                        stream_box.markdown(text)
                except Exception as exc:
                    st.error(
                        "The model call failed. Try a different query or model. "
                        f"\n\nDetails: {exc}"
                    )
                    return

        st.session_state.messages.append({"role": "assistant", "content": text})
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": sources_md,
                "kind": "sources",
                "query": user_query,
            }
        )

    render_sidebar_buttons(st.session_state.messages, on_clear=_clear_history)


if __name__ == "__main__":
    main()
