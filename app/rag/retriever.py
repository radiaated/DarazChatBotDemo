from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import settings


def get_retriever():

    embedding = GoogleGenerativeAIEmbeddings(model=settings.EMBEDDING_MODEL_NAME)

    db = Chroma(
        embedding_function=embedding, persist_directory=settings.VECTOR_STORE_PATH
    )

    retriver = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.4},
    )

    return retriver
