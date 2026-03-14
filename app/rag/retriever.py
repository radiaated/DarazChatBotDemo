from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from config import settings


def get_retriever():
    """
    Initialize and return a retriever from the persisted Chroma vector store.
    """

    # Initialize embedding model
    embedding = GoogleGenerativeAIEmbeddings(model=settings.EMBEDDING_MODEL_NAME)

    # Load existing Chroma vector database
    db = Chroma(
        embedding_function=embedding, persist_directory=settings.VECTOR_STORE_PATH
    )

    # Create retriever with similarity score filtering
    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.4},
    )

    return retriever
