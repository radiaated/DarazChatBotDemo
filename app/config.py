from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Base project path
PROJECT_PATH = os.getcwd()


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # Allowed CORS origins
    ALLOWED_ORIGINS: str

    # Google Gemini API key
    GEMINI_API_KEY: str

    # LLM model name
    MODEL_NAME: str = "gemini-2.5-flash"

    # Embedding model for vector generation
    EMBEDDING_MODEL_NAME: str = "models/gemini-embedding-001"

    # Path to the persisted Chroma vector store
    VECTOR_STORE_PATH: str = os.path.join(PROJECT_PATH, "vectorstore")


# Global settings instance
settings = Settings()
