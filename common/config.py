import os
import streamlit as st
import json
import base64
from streamlit_pdf_viewer import pdf_viewer

base_path = "./data/pdf"
md_path = "./data/md"


# Scan a directory and return a dictionary of folders and files
@st.cache_data
def scan_directory(base_path):
    folders_files = {}
    for folder in os.listdir(base_path):
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

collection_list = [
    "SAP",
    "ASOP_life",
    "CFT",
    "PBR",
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
    "ASOP_life",
    "CFT",
    "PBR",
    "GAAP",
    "IFRS17",
    "Bermuda",
    "Cayman",
    "Asset",
    "Product",
    "RiskFinance (Risk and finance including capital, reinsurance topics)",
    "AI_BigData",
]


@st.cache_data
def get_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


summary_data = get_json("summary.json")


def clear_cache():
    st.cache_data.clear()


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


# def show_pdf(tab, file_path):
#     with tab:
#         st.write(pdf_loader(file_path), unsafe_allow_html=True)


def show_pdf(tab, file_path):
    with tab:
        with st.container(height=600):
            st.write(pdf_viewer(file_path), unsafe_allow_html=True)
