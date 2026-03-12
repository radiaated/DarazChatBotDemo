from langchain_core.prompts import PromptTemplate


def get_prompt():

    prompt = PromptTemplate(
        input_variables=["context", "query"],
        template="""Act as a customer support and answer to all the customer's querys.
Context:
{context}

query: 
{query}
""",
    )

    return prompt
