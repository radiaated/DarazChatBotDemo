from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

import os

load_dotenv()

PROJECT_PATH = os.getcwd()
DOCUMENT_FILE = os.path.join("data", "daraz_faq.pdf")

DOCUMENT_FILE_PATH = os.path.join(PROJECT_PATH, DOCUMENT_FILE)
VECTOR_STORE_PATH = os.path.join(PROJECT_PATH, "app", "vectorstore")


pdf_loader = PyPDFLoader(DOCUMENT_FILE_PATH)


pdf_doc = pdf_loader.load()


splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

# Only two chunks of splitted documents are taken for testing
docs = splitter.split_documents(pdf_doc[:2])

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


db = Chroma.from_documents(
    documents=docs, embedding=embedding, persist_directory=VECTOR_STORE_PATH
)
