# Daraz Chat Bot Demo

⚠️ This is only a demo of a Daraz customer support chatbot and is not affiliated with the official Daraz platform in any way.

---

The Daraz Chat Bot is a customer support chatbot designed to answer customer queries in real time.

This project implements a Retrieval-Augmented Generation (RAG) pipeline that retrieves information from Daraz's FAQ page and uses it to generate accurate responses to customer questions.

## RAG Pipeline

1. **Data Collection**
   Data is collected from Daraz's [FAQ page](https://buyer-helpcenter.daraz.com.np/s/page/category).
   ↓
2. **Data Preprocessing**
   The collected data is cleaned, formatted, and saved as a PDF document.
   ↓
3. **Data loading and Chunking**
   The PDF document is loaded and split into smaller chunks with a token size of `200` and an overlap of `20`.
   ↓
4. **Embedding Generation**
   Each chunk is converted into vector embeddings using the Gemini embedding model `models/gemini-embedding-001`.
   ↓
5. **Vector Database Storage**
   The generated embeddings are stored in the Chroma vector database.
   ↓
6. **User Query Input → Query Embedding**
   The customer's query is converted into an embedding vector using the same embedding model.
   ↓
7. **Retrieval**
   The vector database performs a similarity search and retrieves the top 3 most relevant chunks related to the query.
   ↓
8. **Context Augmentation**
   The retrieved chunks are added to the prompt as context.
   ↓
9. **Response Generation**
   The LLM, Gemini's `gemini-2.5-flash` model, generates the answer using the retrieved context.

## Technology Stack

- RAG
  - LangChain
  - GoogleGenerativeAI
  - Chroma Vectorstore
- Backend
  - FastAPI
- Frontend
  - React
  - TailwindCSS

## Setup

1. Git clone the repo
2. Install Python dependenices
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI development server

   ```
   cd app
   python -m fastapi dev
   ```

4. Install client dependencies and run the React development server
   ```bash
   cd client
   npm i
   npm run dev
   ```

## Usage

- Ingest the data
  Run the ingestion script to process and store the FAQ data in the vector database.

  ```bash
  python scripts/ingest.py
  ```

- API Endpoints
  - REST API

    ```
    /api/chat/chat_bot/
    ```

    - Request Data:

      ```json
      {
        "query": string
      }
      ```

    - Response Data:

      ```json
      {
        "response": string
      }
      ```

  - WebSocket

    ```
    /ws/chat/chat_bot/
    ```

    - Request Data:

      ```json
      {
      "query": string
      }
      ```

    - Response Data:

      ```json
      {
      "response": string
      }
      ```

---

THE END
