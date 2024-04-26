import os
import streamlit as st
import json

base_path = "./data/pdf"


# Define a function to scan a directory and return a dictionary of folders and files.
@st.cache_data  # Add the caching decorator
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


@st.cache_data  # Add the caching decorator
def get_json(file_path):
    # Open and load the json file
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


summary_data = get_json("summary.json")
