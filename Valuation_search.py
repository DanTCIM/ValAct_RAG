from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Actuarial Doc Q&A Model", page_icon="📖", layout="wide")

from valact.settings import (
    ANTHROPIC_MODEL,
    AUTO_OPTION,
    FOLLOWUP_THRESHOLD,
    MAX_CONTEXT_QUESTIONS,
)
from valact.ui import (
    format_sources_block,
    render_chat_history,
    render_disclaimer,
    render_doc_link,
    render_doc_selector,
    render_domain_picker,
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
    st.session_state.pop("pending", None)


def _llm_only_history(messages: list[dict]) -> list[dict]:
    return [
        {"role": m["role"], "content": m["content"]}
        for m in messages
        if m.get("kind") != "sources" and m.get("role") in ("user", "assistant")
    ]


def _prior_context(messages: list[dict]) -> list[str]:
    """Questions behind the previous search, oldest first ([] if none yet)."""
    for m in reversed(messages):
        if m.get("role") == "user":
            return m.get("context") or [m.get("content", "")]
    return []


def _search_context(user_query: str, prior: list[str]) -> list[str]:
    """Questions to search on: the new one, plus the prior ones if Jev reads it
    as a follow-up. Any Jev failure searches on the new question alone."""
    if not prior:
        return [user_query]
    from valact.router import is_followup

    p = is_followup("\n".join(prior), user_query)
    if p is None or p < FOLLOWUP_THRESHOLD:
        return [user_query]
    return (prior + [user_query])[-MAX_CONTEXT_QUESTIONS:]


def _run_rag(
    tab, user_query, search_query, collections, document, num_source, use_mmr, lambda_mult
):
    """Retrieve over the selected collections, then stream the answer.

    Retrieval runs on `search_query` (the question plus any earlier ones it
    follows up on); the answer prompt gets the bare question and the history.
    """
    # Defer heavy SDK imports (anthropic/pinecone/voyageai) until the first
    # query so the page paints before clients load.
    from valact.rag import answer_stream, expand_parents, rerank, retrieve
    from valact.settings import MAX_CONTEXT_PARENTS, RERANK_TOP_N, RETRIEVE_TOP_K

    with tab:
        with st.chat_message("assistant"):
            sources_box = st.container()
            stream_box = st.empty()

            docs = retrieve(
                search_query,
                collections=tuple(collections),
                document=None if document == "All" else document,
                top_k=RETRIEVE_TOP_K,
                use_mmr=use_mmr,
                lambda_mult=lambda_mult,
            )
            reranked = rerank(search_query, docs, top_n=RERANK_TOP_N)
            parents = expand_parents(reranked, max_parents=MAX_CONTEXT_PARENTS)

            sources_md = format_sources_block(
                parents,
                num_source,
                collections,
                search_query=search_query if search_query != user_query else None,
            )
            status = sources_box.status("**Context Retrieval**", expanded=False)
            status.markdown(sources_md, unsafe_allow_html=True)
            status.update(state="complete")

            # The user's question is always the last message here: Auto mode
            # appends it before the picker and adds nothing until submit.
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


def main():
    _init_history()
    tab_qa, tab_md = st.tabs(["Q&A", "TXT-doc"])
    render_header(tab_qa)
    render_disclaimer(ANTHROPIC_MODEL)

    collection, document, doc_link = render_doc_selector()
    num_source, use_mmr, lambda_mult = render_rag_params()

    auto_mode = collection == AUTO_OPTION
    if not auto_mode:
        # Leaving Auto abandons any half-answered suggestion.
        st.session_state.pop("pending", None)

    render_chat_history(tab_qa, st.session_state.messages)
    render_doc_link(document, doc_link)
    render_md_viewer(tab_md, collection, document)
    render_summary(document)

    user_query = st.chat_input(
        placeholder="What is your question on the selected collection/document?"
    )

    if user_query:
        prior = _prior_context(st.session_state.messages)
        with tab_qa:
            st.chat_message("user").write(user_query)
            with st.spinner("Reading the question..."):
                context = _search_context(user_query, prior)
        search_query = "\n".join(context)
        st.session_state.messages.append(
            {"role": "user", "content": user_query, "context": context}
        )
        if auto_mode:
            from valact.router import route

            with tab_qa:
                with st.spinner("Finding the most relevant collections..."):
                    routed = route(search_query)
            # A new question replaces any picker still waiting on screen.
            st.session_state.pending = {
                "query": user_query,
                "search_query": search_query,
                "route": routed,
            }
        else:
            _run_rag(
                tab_qa,
                user_query,
                search_query,
                [collection],
                document,
                num_source,
                use_mmr,
                lambda_mult,
            )

    pending = st.session_state.get("pending")
    if auto_mode and pending:
        # The picker lives in a placeholder so that, once submitted, it can be
        # wiped in this same run -- the answer then renders in its place.
        picker_slot = tab_qa.empty()
        selected = render_domain_picker(
            picker_slot.container(),
            pending["route"],
            pending["query"],
            pending["search_query"],
        )
        if selected:
            st.session_state.pop("pending", None)
            picker_slot.empty()
            _run_rag(
                tab_qa,
                pending["query"],
                pending["search_query"],
                selected,
                "All",
                num_source,
                use_mmr,
                lambda_mult,
            )

    render_sidebar_buttons(st.session_state.messages, on_clear=_clear_history)


if __name__ == "__main__":
    main()
