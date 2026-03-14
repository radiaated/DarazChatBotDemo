from pydantic import BaseModel


class ChatQuery(BaseModel):
    """
    Schema for incoming chat query request.
    """

    # User's question or message
    query: str


class ChatResponse(BaseModel):
    """
    Schema for chatbot response.
    """

    # Generated response from the chatbot
    response: str
