from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from schemas.chat_schemas import ChatQuery, ChatResponse
from services.chat_service import resolve_query

# Router for WebSocket-based chat endpoints
chat_ws_router = APIRouter()


@chat_ws_router.websocket("/chat_bot/")
async def chat_bot(ws: WebSocket):
    """
    WebSocket endpoint for real-time chatbot interaction.
    Receives a query and sends back the generated response.
    """

    # Accept WebSocket connection
    await ws.accept()

    try:

        while True:
            # Receive JSON data from client
            data = await ws.receive_json()

            # Validate and parse incoming query
            chat_query = ChatQuery(**data)

            # Generate chatbot response
            response = resolve_query(chat_query.query)

            # Format response using schema
            chat_response = ChatResponse(response=response)

            # Send response back to client
            await ws.send_json(chat_response.model_dump())

    except WebSocketDisconnect:

        # Client disconnected gracefully
        print("Client disconnected")

    except Exception as e:

        # Optional: handle other unexpected errors
        print(f"WebSocket error: {e}")
