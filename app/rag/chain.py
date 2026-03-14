from langchain_core.runnables import RunnableLambda

from rag.retriever import get_retriever
from rag.prompt import get_prompt
from llm.llm import get_llm


def retrieve_relevant_docs(query: str):
    """
    Retrieve relevant documents for the given query and
    return the query with its retrieved context.
    """

    # Initialize retriever
    retriever = get_retriever()

    # Retrieve documents related to the query
    docs = retriever.invoke(query)

    # Combine document contents into a single context string
    docs_content = "".join(doc.page_content for doc in docs)

    return {"query": query, "context": docs_content}


def get_rag_chain():
    """
    Build and return the RAG pipeline chain.
    """

    # Load prompt template and LLM
    prompt = get_prompt()
    model = get_llm()

    # Define RAG chain: retrieve docs → format prompt → generate response
    chain = (
        RunnableLambda(retrieve_relevant_docs)
        | RunnableLambda(
            lambda context_query: prompt.format_prompt(
                context=context_query["context"], query=context_query["query"]
            )
        )
        | model
    )

    return chain
