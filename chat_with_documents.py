import os
import tempfile
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain

# DK
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


st.set_page_config(page_title="LangChain: Chat with Documents", page_icon="🦜")
st.title("🦜 LangChain: Chat with Documents")


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
    def __init__(self, container):
        self.status = container.status("**Context Retrieval**")

    def on_retriever_start(self, serialized: dict, query: str, **kwargs):
        self.status.write(f"**Question:** {query}")
        self.status.update(label=f"**Context Retrieval:** {query}")

    def on_retriever_end(self, documents, **kwargs):
        for idx, doc in enumerate(documents):
            source = os.path.basename(doc.metadata["source"])
            page = doc.metadata["page"] + 1
            self.status.write(f"**Source: {idx+1} from {source}, page {page}**")
            self.status.markdown(doc.page_content)
        self.status.update(state="complete")


openai_api_key = st.secrets["OPENAI_API_KEY"]
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()

# retriever = configure_retriever(uploaded_files)

# Setup memory for contextual conversation
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=msgs,
    return_messages=True,
    # output_key="output",
)

# Setup LLM and QA chain
llm = ChatOpenAI(
    model_name="gpt-4-0125-preview",
    openai_api_key=openai_api_key,
    temperature=0,
    streaming=True,
)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm, retriever=retriever, memory=memory, verbose=True
)

if len(msgs.messages) == 0 or st.sidebar.button("Clear message history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")

avatars = {"human": "user", "ai": "assistant"}
for msg in msgs.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

if user_query := st.chat_input(placeholder="Ask me anything!"):
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        retrieval_handler = PrintRetrievalHandler(st.container())
        stream_handler = StreamHandler(st.empty())
        response = qa_chain.run(
            user_query, callbacks=[retrieval_handler, stream_handler]
        )
