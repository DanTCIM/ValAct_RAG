# common/handler.py
# Stream + Retrieval UI handler with per-query guard, dedupe, and UI cap

import hashlib
import os
import numpy as np
import streamlit as st

# LangChain 0.2+ prefers langchain_core.*; fall back for older installs.
try:
    from langchain_core.callbacks import BaseCallbackHandler
except ImportError:  # pragma: no cover
    from langchain.callbacks.base import BaseCallbackHandler  # LC < 0.2

from langchain_openai import OpenAIEmbeddings


# ===== Chat model stream handler =====
class StreamHandler(BaseCallbackHandler):
    """
    Streams tokens to a Streamlit container.
    Hides the internal "rephrased" question some chains emit.
    """

    def __init__(
        self, container: st.delta_generator.DeltaGenerator, initial_text: str = ""
    ):
        self.container = container
        self.text = initial_text
        self.run_id_ignore_token = None

    def on_llm_start(self, serialized: dict, prompts: list, **kwargs):
        # Workaround: if a chain sends a "Human: ..." rephrase, don't show it as the answer.
        if prompts and isinstance(prompts, list) and prompts[0].startswith("Human"):
            self.run_id_ignore_token = kwargs.get("run_id")

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        if self.run_id_ignore_token == kwargs.get("run_id", False):
            return
        self.text += token
        self.container.markdown(self.text)


# ===== Retrieval printing handler (UI only) =====
class PrintRetrievalHandler(BaseCallbackHandler):
    """
    Renders retrieved contexts into Streamlit, showing at most `num_source`.
    - Guards against duplicate prints when both base+compression retrievers fire.
    - De-duplicates by (source, page, chunk_id, content hash).
    - (Optional) prints similarity if `calculate_similarity=True`.
    """

    def __init__(self, container, msgs, num_source=5, calculate_similarity=False):
        self.status = container.status("**Context Retrieval**")
        self.msgs = msgs
        self.num_source = int(num_source)
        self.calculate_similarity = calculate_similarity

        self._printed_for_parent_run = None
        self.query_embedding = None
        self.embeddings = (
            OpenAIEmbeddings(model="text-embedding-3-large")
            if calculate_similarity
            else None
        )

    def on_retriever_start(self, serialized: dict, query: str, **kwargs):
        self.status.update(label=f"**Context Retrieval:** {query}")
        self.msgs.add_ai_message(f"Query: {query}")
        if self.calculate_similarity and self.embeddings is not None:
            self.query_embedding = self.embeddings.embed_query(query)

    def on_retriever_end(self, documents, *, run_id=None, parent_run_id=None, **kwargs):
        # --- Guard: print once per query (base retriever + compression retriever can both call this) ---
        pid = parent_run_id or run_id
        if self._printed_for_parent_run == pid:
            return
        self._printed_for_parent_run = pid

        # --- De-duplicate then cap to num_source for UI ---
        seen, unique_docs = set(), []
        for d in documents or []:
            key = (
                d.metadata.get("source"),
                d.metadata.get("page"),
                d.metadata.get("chunk_id"),
                hashlib.md5(d.page_content.strip().encode("utf-8")).hexdigest(),
            )
            if key in seen:
                continue
            seen.add(key)
            unique_docs.append(d)
            if len(unique_docs) >= self.num_source:
                break

        # --- Render into the expander and into chat history ---
        source_msgs = ""
        for idx, doc in enumerate(unique_docs):
            source = os.path.basename(doc.metadata.get("source", ""))
            page_txt = ""  # Add page display if you have it: f", page {doc.metadata.get('page', 0) + 1}"
            contents = doc.page_content

            similarity_txt = ""
            if self.calculate_similarity and self.query_embedding is not None:
                # NOTE: using embed_query for both query+content is fast; for highest fidelity use embed_documents
                content_embedding = self.embeddings.embed_query(contents)
                sim = np.dot(self.query_embedding, content_embedding) / (
                    np.linalg.norm(self.query_embedding)
                    * np.linalg.norm(content_embedding)
                )
                similarity_txt = f"\n* **Similarity score: {round(sim * 100)}%**"

            source_msg = (
                f"# Retrieval {idx+1}\n"
                f"* **Document: {source}{page_txt}**{similarity_txt}\n\n"
                f"{contents}\n\n"
            )
            self.status.write(source_msg, unsafe_allow_html=True)
            source_msgs += source_msg

        # Save the whole rendered block in chat history so your expander shows it later
        self.msgs.add_ai_message(source_msgs)
        self.status.update(state="complete")
