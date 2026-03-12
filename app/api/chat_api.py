from fastapi import APIRouter

from schemas.chat_schemas import ChatQuery, ChatResponse
from services.chat_service import resolve_query

chat_api_router = APIRouter()


@chat_api_router.post("/chat_bot/", response_model=ChatResponse)
async def chat_bot(chat_query: ChatQuery):

    response = resolve_query(chat_query.query)

    return {"response": response}
