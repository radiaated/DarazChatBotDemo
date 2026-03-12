from fastapi import APIRouter, WebSocket
from schemas.chat_schemas import ChatQuery, ChatResponse
from services.chat_service import resolve_query


chat_ws_router = APIRouter()


@chat_ws_router.websocket("/chat_bot/")
async def chat_bot(ws: WebSocket):

    await ws.accept()

    while True:

        data = await ws.receive_json()

        chat_query = ChatQuery(**data)

        response = resolve_query(chat_query.query)

        chat_response = ChatResponse(response=response)

        await ws.send_json(chat_response.model_dump())
