# sqlite3 related (for Streamlit)
# import pysqlite3
# import sys

# sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain

# DK
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import pandas as pd

st.set_page_config(page_title="Actuarial Doc Q&A Model", page_icon="📖")

st.header(
    "Life Actuarial Document Q&A Machine using Retrieval Augmented Generation (RAG)"
)
st.write(
    "Please see the sidebar to select a collection of documents. You can choose a specific document for an exclusive search within that document only."
)

## Set file names as a dictionary
base_path = "./data"


@st.cache_data  # Add the caching decorator
def scan_directory(base_path):
    folders_files = {}
    for folder in os.listdir(base_path):
        if folder == "chroma":  # Skip the "chroma" folder
            continue
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            files = ["All"]
            for file in os.listdir(folder_path):
                # Exclude system files like .DS_Store
                if file != ".DS_Store":
                    files.append(file)
            files[1:] = sorted(files[1:])
            folders_files[folder] = files
    return folders_files


document_list = scan_directory(base_path)
collection_list = ["ASOP_life", "CFT", "VM21", "VM22", "Asset", "Bermuda", "IFRS17"]

with st.sidebar:
    st.title("Life Valuation Actuary Document Q&A Machine")
    st.write("**Built for educational purposes only.**")
    st.write(
        "Powered by OpenAI's GPT 3.5-Turbo: Harness the capabilities of LLM to search for and retrieve information on actuarial documents."
    )

    collection_name = st.selectbox(
        "Select your document collection",
        collection_list,
        # ("ASOP_life", "CFT", "VM21", "VM22", "Asset", "Bermuda", "IFRS17"),
    )

    document_name = st.selectbox(
        "Select your document ",
        document_list[collection_name],
    )

    with st.container(border=True):
        st.subheader("⚙️ RAG Parameters")
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

vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="./data/chroma",
    collection_name=collection_name,
)

# # Retrieve and RAG chain
# Create a retriever using the vector database as the search source
search_kwargs = {"k": num_source}

# Only add the filter if the value is not "All"
if document_name != "All":
    search_kwargs["filter"] = {"source": document_name}

if flag_mmr:
    retriever = vectorstore.as_retriever(
        search_type="mmr", search_kwargs={**search_kwargs, "lambda_mult": _lambda_mult}
    )
    # Use MMR (Maximum Marginal Relevance) to find a set of documents
    # that are both similar to the input query and diverse among themselves
    # Increase the number of documents to get, and increase diversity
    # (lambda mult 0.5 being default, 0 being the most diverse, 1 being the least)
else:
    retriever = vectorstore.as_retriever(
        search_kwargs=search_kwargs
    )  # use similarity search


class StreamHandler(BaseCallbackHandler):
    def __init__(
        self, container: st.delta_generator.DeltaGenerator, initial_text: str = ""
    ):
        self.container = container
        self.text = initial_text
        self.run_id_ignore_token = None

    def on_llm_start(self, serialized: dict, prompts: list, **kwargs):
        # Workaround to prevent showing the rephrased question as output
        if prompts[0].startswith("Human"):
            self.run_id_ignore_token = kwargs.get("run_id")

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        if self.run_id_ignore_token == kwargs.get("run_id", False):
            return
        self.text += token
        self.container.markdown(self.text)


class PrintRetrievalHandler(BaseCallbackHandler):
    def __init__(self, container, msgs):
        self.status = container.status("**Context Retrieval**")
        self.msgs = msgs

    def on_retriever_start(self, serialized: dict, query: str, **kwargs):
        self.status.write(f"**Question:** {query}")
        self.status.update(label=f"**Context Retrieval:** {query}")
        self.msgs.add_ai_message(f"Query**Context retrieval question:** {query}")

    def on_retriever_end(self, documents, **kwargs):
        source_msgs = ""
        for idx, doc in enumerate(documents):
            source = os.path.basename(doc.metadata["source"])
            page = doc.metadata["page"] + 1
            contents = doc.page_content
            source_msg = f"**Source {idx+1}: {source}, page {page}**\n\n {contents}\n\n"
            self.status.write(source_msg)
            source_msgs += source_msg
        self.msgs.add_ai_message(source_msgs)
        self.status.update(state="complete")


openai_api_key = st.secrets["OPENAI_API_KEY"]

# Setup memory for contextual conversation
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=msgs,
    return_messages=True,
)

# Setup LLM and QA chain
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",  ##gpt-4-0125-preview
    openai_api_key=openai_api_key,
    temperature=0,
    streaming=True,
)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm, retriever=retriever, memory=memory, verbose=True
)

if len(msgs.messages) == 0:
    msgs.clear()
    msgs.add_ai_message("How can I help you?")

avatars = {"human": "user", "ai": "assistant"}
for msg in msgs.messages:
    if msg.content.startswith("**Source"):
        with st.expander("**Context Retrieval:**", expanded=False):
            st.write(msg.content)
    elif msg.content.startswith("Query"):
        st.chat_message("assistant", avatar="ℹ️").write(msg.content.lstrip("Query"))
    else:
        st.chat_message(avatars[msg.type]).write(msg.content)
if document_name != "All":
    pdf_file_path = base_path + "/" + collection_name + "/" + document_name
    # Open the file in binary mode
    with open(pdf_file_path, "rb") as pdf_file:
        # Read the PDF file's binary data
        pdf_bytes = pdf_file.read()

        # Create the download button
        st.sidebar.download_button(
            label="Download selected document",
            data=pdf_bytes,
            file_name=pdf_file_path,
            mime="application/octet-stream",
            use_container_width=True,
        )
    if st.sidebar.button(
        "Get main themes",
        use_container_width=True,
    ):
        user_query = "What are the main themes of the documents?"
        st.chat_message("user").write(user_query)
        with st.chat_message("assistant"):
            retrieval_handler = PrintRetrievalHandler(st.container(), msgs)
            stream_handler = StreamHandler(st.empty())
            response = qa_chain.run(
                user_query, callbacks=[retrieval_handler, stream_handler]
            )

if user_query := st.chat_input(placeholder="Ask me anything!"):
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        retrieval_handler = PrintRetrievalHandler(st.container(), msgs)
        stream_handler = StreamHandler(st.empty())
        response = qa_chain.run(
            user_query, callbacks=[retrieval_handler, stream_handler]
        )

with st.sidebar:
    col1, col2 = st.columns(2)
    with col1:

        def clear_chat_history():
            msgs.clear()
            msgs.add_ai_message("How can I help you?")

        st.button(
            label="Clear history",
            use_container_width=True,
            on_click=clear_chat_history,
            help="Clear chat history",
        )
    with col2:

        def convert_df():
            df = pd.DataFrame(msgs.messages)
            return df.to_csv().encode("utf-8")

        st.download_button(
            label="Download",
            help="Download chat history in CSV",
            data=convert_df(),
            file_name="chat_history.csv",
            mime="text/csv",
            use_container_width=True,
        )
