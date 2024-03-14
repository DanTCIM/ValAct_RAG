## sqlite3 related (for Streamlit)
import pysqlite3
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import os
import streamlit as st

# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import pandas as pd

# Start Streamlit session
st.set_page_config(page_title="Actuarial Doc Q&A Model", page_icon="📖")

st.header(
    "Life Actuarial Document Q&A Machine using Retrieval Augmented Generation (RAG)"
)
st.write(
    "Please see the sidebar to select a collection of documents. You can choose a specific document for an exclusive search within that document only."
)

# Set variables
base_path = "./data"
# LLM flag for augmented generation (always use OpenAI embeddings)
USE_Anthropic = True

if USE_Anthropic:
    model_name = "claude-3-sonnet-20240229"
else:
    # model_name = "gpt-3.5-turbo"
    model_name = "gpt-4-0125-preview"


# Define a function to scan a directory and return a dictionary of folders and files.
@st.cache_data  # Add the caching decorator
def scan_directory(base_path):
    folders_files = {}
    for folder in os.listdir(base_path):
        if folder == "chroma_semantic":  # Skip the "chroma" folder
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

## Sidebar
with st.sidebar:
    st.header("**Show me the evidence, AI**")
    st.write(
        f"The *{model_name}*-powered RAG process searches for and retrieves information on actuarial documents. Harness its power but **with accountability and responsibility**."
    )
    st.write(
        "**AI's responses should not be relied upon as accurate or error-free.** The quality of the retrieved contexts and responses may depend on LLM algorithms, RAG parameters, and how questions are asked."
    )
    st.write(
        "Actuaries are strongly advised to **evaluate for accuracy** when using AI. Download the documents to read and review the source. Read the retrieved contexts to compare to AI's responses. The process is built for educational purposes only."
    )

    collection_name = st.selectbox(
        "Select your document collection",
        collection_list,
    )

    document_name = st.selectbox(
        "Select your document",
        document_list[collection_name],
    )

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

# Create a vector store for the document collection
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-large"),
    persist_directory="./data/chroma_semantic",
    collection_name=collection_name,
)

# Retrieve and RAG chain
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


# Chat model stream handler
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


# Retrieval handler
class PrintRetrievalHandler(BaseCallbackHandler):
    def __init__(self, container, msgs):
        self.status = container.status("**Context Retrieval**")
        self.msgs = msgs

    def on_retriever_start(self, serialized: dict, query: str, **kwargs):
        self.status.write(f"**Question:** {query}")
        self.status.update(label=f"**Context Retrieval:** {query}")
        self.msgs.add_ai_message(f"Query: {query}")

    def on_retriever_end(self, documents, **kwargs):
        source_msgs = ""
        for idx, doc in enumerate(documents):
            source = os.path.basename(doc.metadata["source"])
            # page = doc.metadata["page"] + 1
            contents = doc.page_content
            # source_msg = f"**Source {idx+1}: {source}, page {page}**\n\n {contents}\n\n"
            # source_msg = f"**Source {idx+1}: {source}**\n\n {contents}\n\n"
            source_msg = f'<span style="color: navy; font-size: 24px; font-weight: bold;">Source {idx+1}: {source}</span><br> {contents}<br><br>'

            self.status.write(source_msg, unsafe_allow_html=True)
            source_msgs += source_msg
        self.msgs.add_ai_message(source_msgs)
        self.status.update(state="complete")


# Setup memory for contextual conversation
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=msgs,
    return_messages=True,
)

# Setup LLM and QA chain
if USE_Anthropic:
    llm = ChatAnthropic(
        model_name=model_name,
        anthropic_api_key=st.secrets["ANTHROPIC_API_KEY"],
        temperature=0,
        streaming=True,
    )
else:
    llm_notUsed = ChatOpenAI(
        model_name=model_name,
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        temperature=0,
        streaming=True,
    )

qa_chain = ConversationalRetrievalChain.from_llm(
    llm, retriever=retriever, memory=memory, verbose=True
)


# Initialize the chat history
if len(msgs.messages) == 0:
    msgs.add_ai_message("Welcome to life actuarial document Q&A machine!")

# Show the chat history
tmp_query = ""
avatars = {"human": "user", "ai": "assistant"}
for msg in msgs.messages:
    if msg.content.startswith("Query:"):
        tmp_query = msg.content.lstrip("Query: ")
    elif msg.content.startswith("<span style"):
        with st.expander(f"📖 **Context Retrieval:** {tmp_query}", expanded=False):
            st.write(msg.content, unsafe_allow_html=True)
    else:
        tmp_query = ""
        st.chat_message(avatars[msg.type]).write(msg.content)

# Download or get the main themes of the selected document
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
        "Get main themes of selected document",
        use_container_width=True,
    ):
        user_query = (
            "What are the main themes in the document named " + document_name + "?"
        )
        st.chat_message("user").write(user_query)
        with st.chat_message("assistant"):
            retrieval_handler = PrintRetrievalHandler(st.container(), msgs)
            stream_handler = StreamHandler(st.empty())
            response = qa_chain.run(
                user_query, callbacks=[retrieval_handler, stream_handler]
            )

# Ask the user for a question
if user_query := st.chat_input(
    placeholder="What is your question on the selected collection/document?"
):
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        retrieval_handler = PrintRetrievalHandler(st.container(), msgs)
        stream_handler = StreamHandler(st.empty())
        response = qa_chain.run(
            user_query, callbacks=[retrieval_handler, stream_handler]
        )

# Clear chat history or download the chat history in CSV
with st.sidebar:
    col1, col2 = st.columns(2)
    with col1:

        def clear_chat_history():
            msgs.clear()
            msgs.add_ai_message("Welcome to life actuarial document Q&A machine!")

        st.button(
            label="Clear history",
            use_container_width=True,
            on_click=clear_chat_history,
            help="Retrievals use your conversation history, which will influence future outcomes. Clear history to start fresh on a new topic.",
        )
    with col2:

        def convert_df(msgs):
            df = []
            for msg in msgs.messages:
                df.append({"type": msg.type, "content": msg.content})

            df = pd.DataFrame(df)
            return df.to_csv().encode("utf-8")

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
