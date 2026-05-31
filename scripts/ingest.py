from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
import requests

import os

# Load environment variables from .env file
load_dotenv()

# Project paths
PROJECT_PATH = os.getcwd()
DOCUMENT_FILE_PATH = os.path.join(PROJECT_PATH, "data", "daraz_faq.pdf")
VECTOR_STORE_PATH = os.path.join(PROJECT_PATH, "app", "vectorstore")

# Chroma cloud configurations
CHROMA_BASE_URL = os.getenv("CHROMA_BASE_URL")
CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
CHROMA_TENANT = os.getenv("CHROMA_TENANT")
CHROMA_DATABASE = os.getenv("CHROMA_DATABASE")
CHROMA_COLLECTION_ID = os.getenv("CHROMA_COLLECTION_ID")


def ingest():
    """
    Load a PDF document, split it into chunks, generate embeddings,
    and store them in a Chroma vector database.
    """

    try:
        print("[*] Loading PDF document...")

        # Load PDF file
        pdf_loader = PyPDFLoader(DOCUMENT_FILE_PATH)
        pdf_doc = pdf_loader.load()

        print("[✓] PDF document loaded successfully.")

        print("[*] Converting documents into chunks...")

        # Split document into smaller chunks for embedding
        splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

        # Only first two pages used for testing
        docs = splitter.split_documents(pdf_doc[:2])

        print("[✓] Converted documents into chunks successfully.")

        # Initialize embedding model
        embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

        texts = [doc.page_content for doc in docs]
        embeddings = embedding.embed_documents(texts)

        print("[*] Saving chroma vector database from documents and embeddings...")

        # Create and persist remote Chroma vector store

        headers = {
            "x-chroma-token": CHROMA_API_KEY,
            "Content-Type": "application/json",
        }
        payload = {
            "ids": [f"doc_{i}" for i in range(len(texts))],
            "documents": texts,
            "embeddings": embeddings,
            "metadatas": [doc.metadata for doc in docs],
        }

        response = requests.post(
            f"{CHROMA_BASE_URL}/api/v2/tenants/{CHROMA_TENANT}/databases/{CHROMA_DATABASE}/collections/{CHROMA_COLLECTION_ID}/add",
            headers=headers,
            json=payload,
        )

        print("[*] Chromadb cloud response:")

        print("\tResponse status:", response.status_code)
        print("\tResponse message:", response.text)

        print("[✓] Chroma vector database saved.")

    except Exception as ex:
        # Print error if ingestion fails
        print(ex)


if __name__ == "__main__":
    # Run ingestion pipeline
    ingest()
