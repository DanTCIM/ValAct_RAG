# Set up
import dotenv
import os
import json
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain

dotenv.load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")


def setup_llm_chain():
    llm = ChatAnthropic(model_name="claude-opus-4-1-20250805", temperature=0)

    prompt_template = """Write a summary of the following document using the format provided. The summary includes the title, publisher and published date if available, purpose and scope, key points, conclusion and implications, and key words. The summary should be comprehensive yet brief, aiming for a reading time of no more than one minute. Avoid any translation or substitution of actuarial terms in the document. When starting a summary, begin the summary with "Title:" without saying "Here is a summary". Here is the summary format:

    Title: [title of the document]\n\nPublisher and Published Date: [published date and publisher's name]\n\nPurpose and Scope: [note the purpose and scope]\n\nKey Points:\n- [indicate key points in bullet point format]\n\nConclusions and Implications: [describe conclusion and implications for regulatory and practical purposes in the actuarial field]\n\nKey words: [indicate top five key words from the document]

    Here is the document to summarize:

    "{text}"
    """
    prompt = PromptTemplate.from_template(prompt_template)

    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")


def load_existing_results(pathname):
    if os.path.exists(pathname):
        with open(pathname, "r") as f:
            return json.load(f)
    else:
        return {}


def save_results(pathname, results):
    with open(pathname, "w") as f:
        json.dump(results, f, indent=4)


def summarize_collection(collection_name, stuff_chain, results):
    collection_dir = f"./data/upload/md/{collection_name}"
    for file_name in os.listdir(collection_dir):
        if file_name.endswith(".md"):
            md_path = os.path.join(collection_dir, file_name)
            loader = UnstructuredMarkdownLoader(md_path)
            doc = loader.load()
            output = stuff_chain.invoke(doc)
            record = {
                "collection_name": collection_name,
                "summary": output["output_text"],
            }
            file_name_pdf = file_name.replace(".md", ".pdf")
            results[file_name_pdf] = record
    return results


def summarize_collections(pathname, collection_list):
    stuff_chain = setup_llm_chain()
    results = load_existing_results(pathname)

    for collection_name in collection_list:
        results = summarize_collection(collection_name, stuff_chain, results)

    save_results(pathname, results)
