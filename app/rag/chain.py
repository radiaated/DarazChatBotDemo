from langchain_google_genai import GoogleGenerativeAI
from retriever import get_retriever
from prompt import get_prompt
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()


model = GoogleGenerativeAI(model="gemini-2.5-flash")


def get_rag_chain():

    retriever = get_retriever()
    prompt = get_prompt()

    chain = (
        RunnableLambda(lambda x: {"question": x, "docs": retriever.invoke(x)})
        | RunnableLambda(
            lambda x: prompt.format_prompt(
                **{
                    "context": "".join(list(map(lambda x: x.page_content, x["docs"]))),
                    "question": x["question"],
                }
            )
        )
        | RunnableLambda(lambda x: model.invoke(x))
    )

    return chain


# chain = get_rag_chain()

# a = chain.invoke("Are there any offers for a new Daraz user")

# print(a)
