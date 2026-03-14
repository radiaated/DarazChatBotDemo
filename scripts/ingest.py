from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

import os

load_dotenv()

PROJECT_PATH = os.getcwd()

DOCUMENT_FILE_PATH = os.path.join(PROJECT_PATH, "data", "daraz_faq.pdf")
VECTOR_STORE_PATH = os.path.join(PROJECT_PATH, "app", "vectorstore")


def ingest():

    pdf_loader = PyPDFLoader(DOCUMENT_FILE_PATH)

    pdf_doc = pdf_loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

    # Only two chunks of splitted documents are taken for testing
    docs = splitter.split_documents(pdf_doc[:2])

    embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    Chroma.from_documents(
        documents=docs, embedding=embedding, persist_directory=VECTOR_STORE_PATH
    )


if __name__ == "__main__":

    ingest()
