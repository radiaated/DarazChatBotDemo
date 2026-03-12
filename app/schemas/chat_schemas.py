from pydantic import BaseModel


class ChatQuery(BaseModel):

    query: str


class ChatResponse(BaseModel):

    response: str
