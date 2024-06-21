import streamlit as st


def main():
    st.set_page_config(page_title="FAQ", page_icon="📖")

    st.title("Frequently Asked Questions")

    with st.expander("What is RAG?"):
        st.write(
            """
            RAG stands for Retrieval-Augmented Generation. It is a technique used in natural language processing (NLP) that combines the capabilities of a retrieval system and a generative language model. The retrieval system is used to find relevant information from a corpus of documents based on the input query, while the language model is used to generate a response based on the retrieved information and the query.
        """
        )

    with st.expander("Is RAG accurate?"):
        st.write(
            """
            RAG is typically more accurate and provides more relevant responses compared to a generic question asked on a language model alone. However, RAG is not perfect due to potential errors in the retrieval process and limitations of the generative model. Additionally, language models may provide definite answers where the initial question may not have a clear or definitive answer. This "false precision" and "false fluency" is a limitation that RAG also shares with language models.
            """
        )

    with st.expander(
        "What is the difference between RAG and traditional information retrieval?"
    ):
        st.write(
            """
            Traditional information retrieval systems typically retrieve relevant documents or passages based on keyword matching or other statistical methods. RAG, on the other hand, combines the retrieval process with a generative language model, allowing for more natural and context-aware responses. The language model can synthesize information from multiple retrieved sources, fill in gaps, and generate coherent and fluent responses.
        """
        )

    with st.expander("What large language model (LLM) is used?"):
        st.write(
            """
            The application uses Anthropic's Claude 3.5 Sonnet model for generating responses. The model is chosen due to its ability to get input size as large as 200 thousand tokens (about 400-500 pages of texts). Claude 3 is also used to develop the summary of each document.
        """
        )

    with st.expander("What is embedding?"):
        st.write(
            """
            Embedding is the process of converting text data (words, sentences, documents) into high-dimensional vector representations. These vector representations capture the semantic meaning and context of the text data, allowing for efficient storage, retrieval, and comparison of the text using vector operations.
        """
        )

    with st.expander("What embedding model is used?"):
        st.write(
            "This application uses the OpenAI embeddings large model for generating text embeddings."
        )

    with st.expander("What is a vector database?"):
        st.write(
            """
            A vector database is a specialized database designed for storing and querying high-dimensional vector representations (embeddings) of data. Unlike traditional databases that store structured data, vector databases are optimized for working with dense vector representations, enabling efficient similarity searches, nearest neighbor queries, and other vector operations.
        """
        )

    with st.expander("What vector database is used?"):
        st.write(
            """
            Pinecone vector database is used in this application. While open-source databases such as Chroma can be utilized, Pinecone is chosen for its scalability and serverless features. Pinecone is a managed vector database that allows for efficient storage and retrieval of high-dimensional vectors, making it suitable for applications dealing with large-scale vector data. Its serverless architecture, hosted on AWS, eliminates the need for managing infrastructure, enabling developers to focus on building the application. 
        """
        )

    with st.expander(
        "What does the vector database look like? How does it work with retrieval?"
    ):
        st.write(
            """
            A vector database contains embeddings for each document or chunk of text. The database is organized into separate collections. A query is performed within a specific collection. For each document, the text is split into smaller chunks. Each chunk contains metadata, such as the document name. An embedding model assigns a dense vector representation (embedding) to each chunk. These embeddings are then stored in the corresponding collection. 

            During the retrieval process, the user's query is also embedded using the same embedding model. The query embedding is then compared against the embeddings in the database using a similarity metric like cosine similarity. The chunks or documents with embeddings most similar to the query embedding are retrieved as the most relevant results.
        """
        )

    with st.expander(
        "What are considerations when splitting a document into chunks? What method did the application use?"
    ):
        st.write(
            """
            One can use a fixed number of tokens or pages as a straightforward method for chunking, but the application chose to use an embedding similarity method. This approach aims to create more coherent and semantically meaningful chunks by grouping text based on their embeddings' similarity.

            A fixed number of tokens or pages can be used for chunking, and this can be computationally cheaper. Generally, smaller chunks are preferred for question-answering applications where precise retrieval is crucial, while larger chunks may be better suited for summarization or information extraction tasks that require more context.
        """
        )


if __name__ == "__main__":
    main()
