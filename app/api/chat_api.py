from fastapi import APIRouter

from schemas.chat_schemas import ChatQuery, ChatResponse
from services.chat_service import resolve_query

# Create router for chat related endpoints
chat_api_router = APIRouter()


@chat_api_router.post("/chat_bot/", response_model=ChatResponse)
async def chat_bot(chat_query: ChatQuery):
    """
    Chatbot API endpoint.

    Accepts a user query and returns the chatbot response.
    """

    # Process user query using chat service
    response = resolve_query(chat_query.query)

    # Return response in the defined schema format
    return {"response": response}
