# Daraz Chat Bot Demo

⚠️ This is only a demo of a Daraz customer support chatbot and is not affiliated with the official Daraz platform in any way.

---

The Daraz Chat Bot is a customer support chatbot designed to answer customer queries in real time.

This project implements a Retrieval-Augmented Generation (RAG) pipeline that retrieves information from Daraz's FAQ page and uses it to generate accurate responses to customer questions.

## RAG Pipeline

1. **Data Collection** <br />
   Data is collected from Daraz's [FAQ page](https://buyer-helpcenter.daraz.com.np/s/page/category). <br />
   ↓
2. **Data Preprocessing** <br />
   The collected data is cleaned, formatted, and saved as a PDF document. <br />
   ↓
3. **Data loading and Chunking** <br />
   The [PDF document](https://github.com/radiaated/DarazChatBotDemo/blob/main/data/daraz_faq.pdf) is loaded and split into smaller chunks with a token size of `200` and an overlap of `20`. <br />
   ↓
4. **Embedding Generation** <br />
   Each chunk is converted into vector embeddings using the Gemini embedding model `models/gemini-embedding-001`. <br />
   ↓
5. **Vector Database Storage** <br />
   The generated embeddings are stored in the Chroma vector database. <br />
   ↓
6. **User Query Input → Query Embedding** <br />
   The customer's query is converted into an embedding vector using the same embedding model. <br />
   ↓
7. **Retrieval** <br />
   The vector database performs a similarity search and retrieves the top 3 most relevant chunks related to the query. <br />
   ↓
8. **Context Augmentation** <br />
   The retrieved chunks are added to the prompt as context. <br />
   ↓
9. **Response Generation** <br />
   The LLM, Gemini's `gemini-2.5-flash` model, generates the answer using the retrieved context. <br />

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
