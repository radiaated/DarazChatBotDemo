from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os


def get_retriever():

    PROJECT_PATH = os.getcwd()

    VECTOR_STORE_PATH = os.path.join(PROJECT_PATH, "vectorstore")

    embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    db = Chroma(embedding_function=embedding, persist_directory=VECTOR_STORE_PATH)

    retriver = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.4},
    )

    return retriver
