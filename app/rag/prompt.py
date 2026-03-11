from langchain_core.prompts import PromptTemplate


def get_prompt():

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""Act as a customer support and answer to all the customer's questions.
Context:
{context}

Question: 
{question}
""",
    )

    return prompt
