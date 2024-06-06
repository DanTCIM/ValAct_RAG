import os
import streamlit as st
import json
import base64
from streamlit_pdf_viewer import pdf_viewer

base_path = "./data/pdf"
md_path = "./data/md"

collection_list = [
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

collection = [
    "Statutory Accounting Principles (SAP)",
    "PBR",
    "CFT",
    "ASOP_life",
    "GAAP",
    "IFRS17",
    "Bermuda",
    "Cayman",
    "Asset",
    "Product",
    "RiskFinance (Risk and finance including capital, reinsurance topics)",
    "AI_BigData",
]


@st.cache_data(hash_funcs={float: str})
def get_json(file_path, file_modification_time):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def get_file_modification_time(file_path):
    return os.path.getmtime(file_path)


file_path_summary = "./data/summary.json"
file_path_document_list = "./data/document_list.json"
file_path_document_link = "./data/document_link.json"

summary_data = get_json(
    file_path_summary, get_file_modification_time(file_path_summary)
)
document_list = get_json(
    file_path_document_list, get_file_modification_time(file_path_document_list)
)
document_link = get_json(
    file_path_document_link, get_file_modification_time(file_path_document_link)
)


def clear_cache():
    st.cache_data.clear()


# def setup_doc_selector():
#     with st.sidebar:
#         collection_name = st.selectbox(
#             "Select your document collection",
#             collection_list,
#         )

#         document_name = st.selectbox(
#             "Select your document",
#             document_list[collection_name],
#         )
#     return (
#         collection_name,
#         document_name,
#     )


def md_path_creator(path, collection_name, document_name):
    base_name, _ = os.path.splitext(document_name)
    return os.path.join(path, collection_name, f"{base_name}.md")


def md_loader(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data


def pdf_loader(path):
    with open(path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
    <style>
        .pdf-container {{
            width: 100%;
            height: calc(100vh - 15rem);
            overflow: auto;
        }}
        .pdf-container iframe {{
            width: 100%;
            height: 100%;
        }}
    </style>
    <div class="pdf-container">
        <iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>
    </div>
    """

    return pdf_display


def show_pdf(tab, file_path, width=900):
    with tab:
        with st.container(height=700):
            pdf_content = pdf_viewer(
                input=file_path,
                width=width,
            )

            st.write(pdf_content, unsafe_allow_html=True)


def download_pdf_button(base_path, collection_name, document_name):
    if document_name != "All":
        pdf_file_path = os.path.join(base_path, collection_name, document_name)
        with open(pdf_file_path, "rb") as pdf_file:
            # Read the PDF file's binary data
            pdf_bytes = pdf_file.read()

            # Create the download button
            st.sidebar.download_button(
                label="Download selected document",
                data=pdf_bytes,
                file_name=document_name,
                mime="application/octet-stream",
                use_container_width=True,
            )


def display_summary(document_name):
    if document_name != "All":
        summary = summary_data.get(document_name)
        with st.sidebar.expander("AI generated summary of the document", expanded=True):
            if summary:
                st.write(summary.get("summary", "Summary not available."))
            else:
                st.write(f"Summary of '{document_name}' not found in the file.")
