from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Project paths
PROJECT_PATH = os.getcwd()
DOCUMENT_FILE_PATH = os.path.join(PROJECT_PATH, "data", "daraz_faq.pdf")
VECTOR_STORE_PATH = os.path.join(PROJECT_PATH, "app", "vectorstore")


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

        print("[*] Saving chroma vector database from documents and embeddings...")

        # Create and persist Chroma vector store
        Chroma.from_documents(
            documents=docs, embedding=embedding, persist_directory=VECTOR_STORE_PATH
        )

        print("[✓] Chroma vector database saved.")

    except Exception as ex:
        # Print error if ingestion fails
        print(ex)


if __name__ == "__main__":
    # Run ingestion pipeline
    ingest()
