from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat_api import chat_api_router
from ws.chat_ws import chat_ws_router
from config import settings

# Parse allowed CORS origins from environment settings
ALLOWED_ORIGINS = (
    settings.ALLOWED_ORIGINS.split(",") if settings.ALLOWED_ORIGINS else []
)

# Initialize FastAPI app
app = FastAPI(title="Customer Support Chatbot API")

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include REST API routes
app.include_router(router=chat_api_router, prefix="/api/chat")

# Include WebSocket routes
app.include_router(router=chat_ws_router, prefix="/ws/chat")
