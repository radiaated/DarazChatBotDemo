from langchain_core.prompts import PromptTemplate


def get_prompt():
    """
    Create and return the prompt template used for the RAG pipeline.
    """

    # Define prompt template with context and user query
    prompt = PromptTemplate(
        input_variables=["context", "query"],
        template="""Act as a customer support and answer to all the customer's queries.

Context:
{context}

Query:
{query}
""",
    )

    return prompt
