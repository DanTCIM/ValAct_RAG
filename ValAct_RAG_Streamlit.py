import os
import streamlit as st
from common.config import (
    base_path,
    md_path,
    document_list,
    collection_list,
    md_path_creator,
    md_loader,
    show_pdf,
    display_summary,
    download_pdf_button,
)

from common.handler import (
    StreamHandler,
    PrintRetrievalHandler,
)
from langchain_community.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import pandas as pd


def setup_tabs():
    tab1, tab2, tab3 = st.tabs(["Q&A", "PDF-doc", "TXT-doc"])
    return tab1, tab2, tab3


def display_header(tab):
    with tab:
        st.header(
            "Life Actuarial Document Q&A Machine using Retrieval Augmented Generation (RAG)"
        )
        st.write(
            "Please see the sidebar to select a collection of documents. You can choose a specific document for an exclusive search within that document only."
        )


def setup_sidebar(model_name):
    with st.sidebar:
        with st.expander("**Show me the evidence, AI**"):
            # st.header("**Show me the evidence, AI**")
            st.write(
                f"The *{model_name}*-powered RAG process searches for and retrieves information on actuarial documents. Harness its power but **with accountability and responsibility**."
            )
            st.write(
                "**AI's responses should not be relied upon as accurate or error-free.** The quality of the retrieved contexts and responses may depend on LLM algorithms, RAG parameters, and how questions are asked."
            )
            st.write(
                "Actuaries are strongly advised to **evaluate for accuracy** when using AI. Download the documents to read and review the source. Read the retrieved contexts to compare to AI's responses. The process is built for educational purposes only."
            )


def setup_doc_selector():
    with st.sidebar:
        collection_name = st.selectbox(
            "Select your document collection",
            collection_list,
        )

        document_name = st.selectbox(
            "Select your document",
            document_list[collection_name],
        )
    return (
        collection_name,
        document_name,
    )


def setup_rag_param():
    with st.sidebar:
        with st.expander("⚙️ RAG Parameters"):
            num_source = st.slider(
                "Top N sources to view:", min_value=4, max_value=20, value=5, step=1
            )
            flag_mmr = st.toggle(
                "Diversity search",
                value=True,
                help="Diversity search, i.e., Maximal Marginal Relevance (MMR) tries to reduce redundancy of fetched documents and increase diversity. 0 being the most diverse, 1 being the least diverse. 0.5 is a balanced state.",
            )
            _lambda_mult = st.slider(
                "Diversity parameter (lambda):",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                step=0.25,
            )
            flag_similarity_out = st.toggle(
                "Output similarity score",
                value=False,
                help="The retrieval process may become slower due to the cosine similarity calculations. A similarity score of 100% indicates the highest level of similarity between the query and the retrieved chunk.",
            )
    return (
        num_source,
        flag_mmr,
        _lambda_mult,
        flag_similarity_out,
    )


def setup_vectorstore(collection_name):
    pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])
    vectorstore = PineconeVectorStore(
        index=pc.Index("valact-rag"),
        embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
        namespace=collection_name,
    )
    return vectorstore


def setup_retriever(vectorstore, document_name, num_source, flag_mmr, _lambda_mult):
    search_kwargs = {"k": num_source}

    if document_name != "All":
        search_kwargs["filter"] = {"source": document_name}

    if flag_mmr:
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
        memory_key="chat_history",
        chat_memory=msgs,
        return_messages=True,
    )
    return msgs, memory


def setup_llm(use_anthropic, model_name):
    if use_anthropic:
        llm = ChatAnthropic(
            model_name=model_name,
            anthropic_api_key=st.secrets["ANTHROPIC_API_KEY"],
            temperature=0,
            streaming=True,
        )
    else:
        llm = ChatOpenAI(
            model_name=model_name,
            openai_api_key=st.secrets["OPENAI_API_KEY"],
            temperature=0,
            streaming=True,
        )
    return llm


def setup_qa_chain(llm, retriever, memory):
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm, retriever=retriever, memory=memory, verbose=True
    )
    return qa_chain


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


def display_pdf(tab, document_name, collection_name):
    if document_name == "All":
        with tab:
            st.write(
                "When you select a document and click the button, the app displays the selected PDF."
            )

    else:
        pdf_file_path = os.path.join(base_path, collection_name, document_name)
        st.sidebar.button(
            "Show selected document in tab PDF-doc",
            on_click=lambda: show_pdf(tab, pdf_file_path),
            help="See tab PDF-doc to view the selected PDF.",
            use_container_width=True,
        )


def display_markdown(tab, document_name, collection_name):
    if document_name == "All":
        with tab:
            st.write(
                "When you select a document, the app loads the pre-converted Markdown file and displays the content for your review. Please note that the displayed text, formulas, tables, charts, and images may contain some rendering errors due to the conversion process. To access the original content, download the PDF file using the button in the sidebar."
            )
    else:
        md_file_path = md_path_creator(md_path, collection_name, document_name)
        with tab:
            md_container = st.container(height=700)
            with md_container:
                md_txt = md_loader(md_file_path)
                st.write(md_txt, unsafe_allow_html=True)


def handle_user_query(tab, qa_chain, msgs, flag_similarity_out):
    if user_query := st.chat_input(
        placeholder="What is your question on the selected collection/document?"
    ):
        with tab:
            st.chat_message("user").write(user_query)

            with st.chat_message("assistant"):
                retrieval_handler = PrintRetrievalHandler(
                    st.container(), msgs, calculate_similarity=flag_similarity_out
                )
                stream_handler = StreamHandler(st.empty())
                qa_chain.run(user_query, callbacks=[retrieval_handler, stream_handler])


def clear_chat_history(msgs):
    msgs.clear()
    msgs.add_ai_message("Welcome to life actuarial document Q&A machine!")


def convert_df(msgs):
    df = []
    for msg in msgs.messages:
        df.append({"type": msg.type, "content": msg.content})

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
                help="Retrievals use your conversation history, which will influence future outcomes. Clear history to start fresh on a new topic.",
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

        link = "https://github.com/DanTCIM/ValAct_RAG"
        st.caption(
            f"🖋️ The Python code and documentation of the project are in [GitHub]({link})."
        )


def main():
    st.set_page_config(
        page_title="Actuarial Doc Q&A Model",
        page_icon="📖",
        layout="wide",
    )
    use_anthropic = True
    model_name = "claude-3-sonnet-20240229" if use_anthropic else "gpt-4-turbo"

    tab1, tab2, tab3 = setup_tabs()
    display_header(tab1)
    setup_sidebar(model_name)
    (
        collection_name,
        document_name,
    ) = setup_doc_selector()
    (
        num_source,
        flag_mmr,
        _lambda_mult,
        flag_similarity_out,
    ) = setup_rag_param()

    vectorstore = setup_vectorstore(collection_name)
    retriever = setup_retriever(
        vectorstore, document_name, num_source, flag_mmr, _lambda_mult
    )

    msgs, memory = setup_memory()
    llm = setup_llm(use_anthropic, model_name)
    qa_chain = setup_qa_chain(llm, retriever, memory)

    initialize_chat_history(msgs)
    display_chat_history(tab1, msgs)
    download_pdf_button(base_path, collection_name, document_name)
    display_pdf(tab2, document_name, collection_name)
    display_markdown(tab3, document_name, collection_name)
    display_summary(document_name)
    handle_user_query(tab1, qa_chain, msgs, flag_similarity_out)
    display_sidebar_buttons(msgs)


if __name__ == "__main__":
    main()
