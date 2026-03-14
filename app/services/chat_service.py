from rag.chain import get_rag_chain


def resolve_query(query):
    """
    Process the user query using the RAG chain and return the response.
    """

    # Initialize the RAG pipeline
    chain = get_rag_chain()

    # Generate response from the chain
    response = chain.invoke(query)

    return response
