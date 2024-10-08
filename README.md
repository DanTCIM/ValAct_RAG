# Life Valuation Actuarial Document Q&A machine using Retrieval Augmented Generation (RAG)
## 1. Description
This project aims to create a Retrieval-Augmented Generation (RAG) process for actuaries to ask questions about a set of Life Valuation Actuarial documents. The RAG process utilizes the power of the large language model (LLM) to provide quick answers to questions about the documents.

The collections include:
- [Statutory Accounting Principles](./data/pdf/SAP)
- [Principle-Based Reserving](./data/pdf/PBR)
- [Cash Flow Testing and Asset Adequacy Testing](./data/pdf/CFT)
- [Actuarial Standards of Practice related to Life Insurance](./data/pdf/ASOP_life)
- [US GAAP](./data/pdf/GAAP)
- [IFRS 17](./data/pdf/IFRS17)
- [Bermuda](./data/pdf/Bermuda)
- [Cayman and CIMA documents](./data/pdf/Cayman/)
- [Asset related documents](./data/pdf/Asset)
- [Liability Products](./data/pdf/Product)
- [Risk and Finance including Capital and Reinsurance](./data/pdf/RiskFinance)
- [AI and Big Data](./data/pdf/AI_BigData)

However, RAG is not without challenges, i.e., hallucination and inaccuracy. The project allows verifiability by providing the context an LLM used to arrive at those answers. This process enables actuaries to validate the LLM's answers, empowering them to make informed decisions. By combining the capabilities of LLM with verifiability, this RAG process offers actuaries a robust tool to leverage LLM technology effectively and extract maximum value.

The current example uses Anthropic's Claude 3.5 Sonnet. The context window size is 200k tokens, which makes it suitable for understanding lengthy documents.

The RAG process used LangChain, a framework for developing applications powered by LLMs.

## 2. Output
### 2.1 Demo App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://valact-search.streamlit.app/)  
Explore the potentials of RAG by visiting the Streamlit web app (https://valact-search.streamlit.app/) powered by Claude 3.5.

## 3. Model
### 3.1 Conceptual Flow
RAG combines search and LLM generations.  

LLM completions are the results of model inference based on locked-in parameters. Any knowledge or information from LLM can be outdated unless augmented by external sources. RAG connects external documents, searches the document, and provides the relevant context to LLM. The external documents are transformed into a vector database during the initial setup stage for an effective search.  

For applications in practice, one should note that RAG is not perfect and can still lead to errors in searching or generating irrelevant or incorrect responses. As such, verifiability in RAG becomes crucial for actuarial use cases.

![RAG concept](./images/RAG_concept.png)

### 3.2 RAG Implementation Steps
    1. Select PDF documents from a collection to perform RAG 
    2. Convert PDF into markdown files for effective loading (MathPix service seems superior to open source processes)
    3. Load markdown files to texts and split them into chunks using semantics method
    4. Convert the chunks into a vector database (Chroma DB) using the OpenAI embedding model (text-embedding-3-large)
    5. Retrieve and use LLM to generate
    6. Output responses and context for a user to verify

## 4. Author
Dan Kim 

- [@LinkedIn](https://www.linkedin.com/in/dan-kim-4aaa4b36/)
- dan.kim.actuary@gmail.com (feel free to reach out with questions or comments)

## 5. Date
- Initially published on 3/2/2024
- The contents may be updated from time to time
  
## 6. License
This project is licensed under the Apache License 2.0- see the LICENSE.md file for details.

## 7. Acknowledgments and References
- https://python.langchain.com/docs/use_cases/question_answering/quickstart
- https://python.langchain.com/docs/use_cases/question_answering/sources
- https://chat.langchain.com/
- https://ollama.ai/
- https://www.trychroma.com/
