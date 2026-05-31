from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import settings

import requests


def retrieve_docs(query: str):
    """
    Retrieves the relevant documents from remote Chroma vector store
    """

    try:

        # Initialize embedding model
        embedding = GoogleGenerativeAIEmbeddings(model=settings.EMBEDDING_MODEL_NAME)

        # Embed the query
        embeddings = embedding.embed_documents([query])

        # Query the remote vector database from with query embeddings through http request
        headers = {
            "x-chroma-token": settings.CHROMA_API_KEY,
            "Content-Type": "application/json",
        }
        payload = {
            "include": ["documents"],
            "n_results": 3,
            "query_embeddings": embeddings,
        }

        response = requests.post(
            f"{settings.CHROMA_BASE_URL}/api/v2/tenants/{settings.CHROMA_TENANT}/databases/{settings.CHROMA_DATABASE}/collections/{settings.CHROMA_COLLECTION_ID}/query",
            headers=headers,
            json=payload,
        )

        data = response.json()

        return data["documents"][0]

    except Exception as ex:
        # Print error if ingestion fails
        print(ex)
