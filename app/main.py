from fastapi import FastAPI
from api.chat_api import chat_api_router
from ws.chat_ws import chat_ws_router
from fastapi.middleware.cors import CORSMiddleware

from config import settings


ALLOWED_ORIGINS = (
    settings.ALLOWED_ORIGINS.split(",") if settings.ALLOWED_ORIGINS else []
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=chat_api_router, prefix="/api/chat")
app.include_router(router=chat_ws_router, prefix="/ws/chat")
