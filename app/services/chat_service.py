from rag.chain import get_rag_chain


def resolve_query(query):

    chain = get_rag_chain()

    response = chain.invoke(query)

    return response
