from langchain_google_genai import GoogleGenerativeAI

from config import settings


def get_llm():
    llm = GoogleGenerativeAI(model=settings.MODEL_NAME)

    return llm
