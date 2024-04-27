# Import modules
import glob
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import PyPDFium2Loader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import MathpixPDFLoader
from langchain_community.document_loaders import PDFMinerLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings


# Define a function to load and extract text from PDFs in a folder
def get_file_name(source_path):
    return source_path.split("/")[-1]


def load_pdfs_from_folder(folder_path, loader_option):
    pdf_files = glob.glob(f"{folder_path}/*.pdf")
    docs = []
    for pdf_file in pdf_files:
        file_name = get_file_name(pdf_file)
        loaded_docs = load_pdf_file(pdf_file, loader_option)
        for doc in loaded_docs:
            doc.metadata["source"] = file_name
        docs.extend(loaded_docs)
    return docs


def load_pdf_file(pdf_file, loader_option):
    if loader_option == 1:
        loader = PyPDFLoader(pdf_file)
    elif loader_option == 2:
        loader = PyPDFium2Loader(pdf_file)
    elif loader_option == 3:
        loader = PyMuPDFLoader(pdf_file)
    elif loader_option == 4:
        loader = PDFMinerLoader(pdf_file, concatenate_pages=True)
    elif loader_option == 5:
        loader = MathpixPDFLoader(pdf_file)
    return loader.load()


def pdf_to_md(folder_path, download_path, loader_option):
    pdf_files = glob.glob(f"{folder_path}/*.pdf")
    for pdf_file in pdf_files:
        file_name = get_file_name(pdf_file)
        base_name = file_name.replace(".pdf", "")
        loaded_docs = load_pdf_file(pdf_file, loader_option)
        save_to_md(loaded_docs, file_name, base_name, download_path, loader_option)


def save_to_md(loaded_docs, file_name, base_name, download_path, loader_option):
    for i, doc in enumerate(loaded_docs):
        doc.metadata["source"] = file_name
        if loader_option > 3:
            md_file_name = f"{download_path}/{base_name}.md"
        else:
            md_file_name = f"{download_path}/{base_name}{i+1:03d}.md"
        with open(md_file_name, "w", encoding="utf-8") as md_file:
            md_file.write(doc.page_content)


def load_mds_from_folder(folder_path):
    # Get a list of md files in the specified folder
    md_files = glob.glob(f"{folder_path}/*.md")
    docs = []
    for md_file in md_files:
        file_name = get_file_name(md_file)
        base_name = file_name.replace(".md", "")
        pdf_file_name = f"{base_name}.pdf"

        loader = UnstructuredMarkdownLoader(md_file)
        loaded_docs = loader.load()

        for doc in loaded_docs:
            doc.metadata["source"] = pdf_file_name

        docs.extend(loaded_docs)
    return docs


def split_mds(
    folder_path,
    IsSemantic=False,
    chunk_size_input=3000,
    breakpoint_threshold_type_input="standard_deviation",
    breakpoint_threshold_amount_input=3,
    embeddings_model=OpenAIEmbeddings(model="text-embedding-3-large"),
):
    md_files = glob.glob(f"{folder_path}/*.md")
    all_splits = []
    for md_file in md_files:
        file_name = get_file_name(md_file)
        base_name = file_name.replace(".md", "")
        pdf_file_name = f"{base_name}.pdf"
        loaded_docs = load_md_file(md_file)
        md_header_splits = split_md_by_headers(loaded_docs[0].page_content)
        splits = split_md_by_content(
            md_header_splits,
            IsSemantic,
            chunk_size_input,
            breakpoint_threshold_type_input,
            breakpoint_threshold_amount_input,
            embeddings_model,
        )
        all_splits.extend(add_source_metadata(splits, pdf_file_name))
    return all_splits


def load_md_file(md_file):
    loader = TextLoader(md_file)
    return loader.load()


def split_md_by_headers(page_content):
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
        ("#####", "Header 5"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False,
    )
    return markdown_splitter.split_text(page_content)


def split_md_by_content(
    md_header_splits,
    IsSemantic,
    chunk_size_input,
    breakpoint_threshold_type_input,
    breakpoint_threshold_amount_input,
    embeddings_model,
):
    all_splits = []
    for doc in md_header_splits:
        if len(doc.page_content) > 4000:
            if IsSemantic:
                text_splitter = SemanticChunker(
                    embeddings=embeddings_model,
                    breakpoint_threshold_type=breakpoint_threshold_type_input,
                    breakpoint_threshold_amount=breakpoint_threshold_amount_input,
                )
            else:
                chunk_size = chunk_size_input
                chunk_overlap = 50
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                )
            splits = text_splitter.split_documents([doc])
            all_splits.extend(splits)
        else:
            all_splits.append(doc)
    return all_splits


def add_source_metadata(splits, pdf_file_name):
    for split in splits:
        split.metadata["source"] = pdf_file_name
    return splits
