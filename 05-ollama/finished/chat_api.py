from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import chat

api = FastAPI()


class ChatMessage(BaseModel):
    model: str
    messages: list[dict]


@api.post("/chat")
async def send_chat_message(body: ChatMessage):
    response = chat(model=body.model, messages=body.messages)
    return {
        "response": response["message"]["content"],
    }
