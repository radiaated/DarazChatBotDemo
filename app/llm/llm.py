from langchain_google_genai import GoogleGenerativeAI

from config import settings


def get_llm():
    """
    Initialize and return the Google Generative AI LLM instance.
    """

    # Create LLM using model name from application settings
    llm = GoogleGenerativeAI(model=settings.MODEL_NAME)

    return llm
