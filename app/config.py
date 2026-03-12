from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


PROJECT_PATH = os.getcwd()


class Settings(BaseSettings):

    ALLOWED_ORIGINS: str
    GEMINI_API_KEY: str
    MODEL_NAME: str = "gemini-2.5-flash"
    EMBEDDING_MODEL_NAME: str = "models/gemini-embedding-001"
    VECTOR_STORE_PATH: str = os.path.join(PROJECT_PATH, "vectorstore")


settings = Settings()
