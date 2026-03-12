from langchain_core.runnables import RunnableLambda

from rag.retriever import get_retriever
from rag.prompt import get_prompt
from llm.llm import get_llm


def retrieve_relevant_docs(query: str):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    docs_content = "".join(doc.page_content for doc in docs)

    return {"query": query, "context": docs_content}


def get_rag_chain():

    prompt = get_prompt()
    model = get_llm()

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
