# ValAct_RAG_Streamlit.py
# Main app: keep RAG recall (fetch 80 -> compress 40), LLM sees up to 40 unique chunks,
# UI shows exactly `num_source` from the sidebar.

import streamlit as st

st.set_page_config(page_title="Actuarial Doc Q&A Model", page_icon="📖", layout="wide")

# ---- Your project helpers ----
from common.config import (
    base_path,
    md_path,
    document_list,
    document_link,
    collection_list,
    md_path_creator,
    md_loader,
    display_summary,
)

from common.handler import StreamHandler, PrintRetrievalHandler

# ---- LangChain / Vendors ----
from langchain_openai import ChatOpenAI as OpenAIChat
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import pandas as pd

# LangChain 0.2+ core imports
from typing import List, Optional
import hashlib

from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from pydantic import Field

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter


# ==== RAG retrieval tuning constants (unchanged) ====
FETCH_K = 80  # hidden candidate pool for retrieval (recall)
MAX_CONTEXT_DOCS = 40  # after compression (what the LLM can see, pre-dedupe)
USE_THRESHOLD = False
SCORE_THRESHOLD = 0.1
# ====================================================


# ===== UI scaffolding =====
def setup_tabs():
    return st.tabs(["Q&A", "TXT-doc"])


def display_header(tab):
    with tab:
        st.header(
            "Life Actuarial Document Q&A Machine using Retrieval Augmented Generation (RAG)"
        )
        st.write(
            "Please see the sidebar to select a collection of documents. "
            "You can choose a specific document for an exclusive search within that document only."
        )


def setup_sidebar(model_name):
    with st.sidebar:
        with st.expander("**Show me the evidence, AI**"):
            st.write(
                f"The *{model_name}*-powered RAG process searches for and retrieves information on actuarial documents. "
                "Harness its power but **with accountability and responsibility**."
            )
            st.write(
                "**AI's responses should not be relied upon as accurate or error-free.**"
            )
            st.write(
                "Actuaries are strongly advised to **evaluate for accuracy** when using AI. "
                "Read the source documents. Review the retrieved contexts to compare to AI's responses. "
                "The process is built for educational purposes only."
            )


def setup_doc_selector():
    with st.sidebar:
        collection_name = st.selectbox(
            "Select your document collection", collection_list
        )
        document_name = st.selectbox(
            "Select your document", document_list[collection_name]
        )
        doc_link = document_link[document_name]
    return collection_name, document_name, doc_link


def setup_rag_param():
    with st.sidebar:
        with st.expander("⚙️ RAG Parameters"):
            num_source = st.slider("Top N sources to view:", 4, 20, 5, 1)
            flag_mmr = st.toggle(
                "Diversity search",
                value=True,
                help="Maximal Marginal Relevance (MMR) reduces redundancy and increases diversity.",
            )
            _lambda_mult = st.slider(
                "Diversity parameter (lambda):", 0.0, 1.0, 0.5, 0.25
            )
            flag_similarity_out = st.toggle(
                "Output similarity score",
                value=False,
                help="May be slower due to extra embeddings. 100% = highest similarity.",
            )
    return num_source, flag_mmr, _lambda_mult, flag_similarity_out


def setup_vectorstore(collection_name):
    pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])
    return PineconeVectorStore(
        index=pc.Index("valact-rag"),
        embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
        namespace=collection_name,
    )


def setup_retriever(vectorstore, document_name, flag_mmr, _lambda_mult):
    # Keep a large hidden pool for recall
    search_kwargs = {"k": FETCH_K}
    if document_name != "All":
        search_kwargs["filter"] = {"source": document_name}

    if USE_THRESHOLD:
        retriever = vectorstore.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={**search_kwargs, "score_threshold": SCORE_THRESHOLD},
        )
    elif flag_mmr:
        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={**search_kwargs, "lambda_mult": _lambda_mult},
        )
    else:
        retriever = vectorstore.as_retriever(search_kwargs=search_kwargs)

    return retriever


def setup_memory():
    msgs = StreamlitChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history", chat_memory=msgs, return_messages=True
    )
    return msgs, memory


def setup_llm(use_anthropic: bool, model_name: str):
    if use_anthropic:
        return ChatAnthropic(
            model_name=model_name,
            anthropic_api_key=st.secrets["ANTHROPIC_API_KEY"],
            temperature=0,
            streaming=True,
        )
    else:
        return OpenAIChat(
            model=model_name,
            api_key=st.secrets["OPENAI_API_KEY"],
            # temperature not set for gpt-5 per API constraint
            streaming=True,
        )


def setup_qa_chain(llm, retriever, memory):
    return ConversationalRetrievalChain.from_llm(
        llm, retriever=retriever, memory=memory, verbose=True
    )


def initialize_chat_history(msgs):
    if len(msgs.messages) == 0:
        msgs.add_ai_message("Welcome to life actuarial document Q&A machine!")


def display_chat_history(tab, msgs):
    tmp_query = ""
    avatars = {"human": "user", "ai": "assistant"}
    with tab:
        for msg in msgs.messages:
            if msg.content.startswith("Query:"):
                tmp_query = msg.content.lstrip("Query: ")
            elif msg.content.startswith("# Retrieval"):
                with st.expander(
                    f"📖 **Context Retrieval:** {tmp_query}", expanded=False
                ):
                    st.write(msg.content, unsafe_allow_html=True)
            else:
                tmp_query = ""
                st.chat_message(avatars[msg.type]).write(msg.content)


def display_link(document_name, doc_link):
    if document_name != "All":
        with st.sidebar:
            with st.container(border=True):
                st.write(f"**View Source** (tab TXT-doc or link below): {doc_link}")


def display_markdown(tab, document_name, collection_name):
    if document_name == "All":
        with tab:
            st.write(
                "When you select a document, the app loads the pre-converted Markdown file and displays the content "
                "for your review. The display may contain rendering errors; use the source link in the sidebar."
            )
    else:
        md_file_path = md_path_creator(md_path, collection_name, document_name)
        with tab:
            md_container = st.container(height=700)
            with md_container:
                md_txt = md_loader(md_file_path)
                st.write(md_txt, unsafe_allow_html=True)


def clear_chat_history(msgs):
    msgs.clear()
    msgs.add_ai_message("Welcome to life actuarial document Q&A machine!")


def convert_df(msgs):
    df = [{"type": m.type, "content": m.content} for m in msgs.messages]
    df = pd.DataFrame(df)
    return df.to_csv().encode("utf-8")


def display_sidebar_buttons(msgs):
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                label="Clear history",
                use_container_width=True,
                on_click=clear_chat_history,
                args=(msgs,),
                help="Clear history to start fresh on a new topic.",
            )
        with col2:
            st.download_button(
                label="Download history",
                help="Download chat history in CSV",
                data=convert_df(msgs),
                file_name="chat_history.csv",
                mime="text/csv",
                use_container_width=True,
            )
        st.caption(
            "🖋️ The Python code and documentation of the project are in [GitHub](https://github.com/DanTCIM/ValAct_RAG)."
        )


# ===== Retrieval wrappers =====
def maybe_wrap_with_compression(retriever):
    # Keep LLM capacity at 40 post-compression
    compressor = EmbeddingsFilter(
        embeddings=OpenAIEmbeddings(model="text-embedding-3-large"),
        k=MAX_CONTEXT_DOCS,
    )
    return ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )


class DedupeOnlyRetriever(BaseRetriever):
    """
    Removes duplicate chunks (by source/page/chunk_id/content hash) without slicing the count.
    Lets the LLM see up to MAX_CONTEXT_DOCS unique docs after compression.
    """

    inner: BaseRetriever = Field(...)  # declare as a pydantic field
    model_config = {"arbitrary_types_allowed": True}

    def _uniq(self, docs: List[Document]) -> List[Document]:
        seen, out = set(), []
        for d in docs:
            key = (
                d.metadata.get("source"),
                d.metadata.get("page"),
                d.metadata.get("chunk_id"),
                hashlib.md5(d.page_content.strip().encode("utf-8")).hexdigest(),
            )
            if key in seen:
                continue
            seen.add(key)
            out.append(d)
        return out

    # sync path
    def _get_relevant_documents(
        self,
        query: str,
        *,
        run_manager: Optional[CallbackManagerForRetrieverRun] = None,
    ) -> List[Document]:
        # BEFORE (causes multiple values for run_manager):
        # docs = self.inner.get_relevant_documents(query, run_manager=run_manager)

        # AFTER:
        docs = self.inner.get_relevant_documents(query)
        return self._uniq(docs)

    # async path
    async def _aget_relevant_documents(
        self,
        query: str,
        *,
        run_manager: Optional[CallbackManagerForRetrieverRun] = None,
    ) -> List[Document]:
        # BEFORE:
        # docs = await self.inner.aget_relevant_documents(query, run_manager=run_manager)

        # AFTER:
        docs = await self.inner.aget_relevant_documents(query)
        return self._uniq(docs)


# ===== Query handling =====
def handle_user_query(tab, qa_chain, msgs, flag_similarity_out, num_source):
    """
    - Streams LLM output
    - Prints retrieval contexts (deduped & UI-capped to num_source)
    """
    if user_query := st.chat_input(
        placeholder="What is your question on the selected collection/document?"
    ):
        with tab:
            st.chat_message("user").write(user_query)
            with st.chat_message("assistant"):
                retrieval_handler = PrintRetrievalHandler(
                    st.container(),
                    msgs,
                    num_source=num_source,  # UI cap here
                    calculate_similarity=flag_similarity_out,  # optional similarity calc
                )
                stream_handler = StreamHandler(st.empty())
                qa_chain.run(user_query, callbacks=[retrieval_handler, stream_handler])


# ===== Main =====
def main():
    use_anthropic = True
    model_name = "claude-opus-4-1-20250805" if use_anthropic else "gpt-5"
    # claude-3-7-sonnet-20250219
    # claude-3-5-sonnet-20241022
    # claude-opus-4-1-20250805
    # claude-sonnet-4-20250514

    tab1, tab2 = setup_tabs()
    display_header(tab1)
    setup_sidebar(model_name)

    collection_name, document_name, doc_link = setup_doc_selector()
    num_source, flag_mmr, _lambda_mult, flag_similarity_out = setup_rag_param()

    vectorstore = setup_vectorstore(collection_name)
    base = setup_retriever(vectorstore, document_name, flag_mmr, _lambda_mult)
    compressed = maybe_wrap_with_compression(base)  # k = 40
    retriever = DedupeOnlyRetriever(inner=compressed)

    msgs, memory = setup_memory()
    llm = setup_llm(use_anthropic, model_name)
    qa_chain = setup_qa_chain(llm, retriever, memory)

    initialize_chat_history(msgs)
    display_chat_history(tab1, msgs)
    display_link(document_name, doc_link)
    display_markdown(tab2, document_name, collection_name)
    display_summary(document_name)

    handle_user_query(tab1, qa_chain, msgs, flag_similarity_out, num_source)
    display_sidebar_buttons(msgs)


if __name__ == "__main__":
    main()
