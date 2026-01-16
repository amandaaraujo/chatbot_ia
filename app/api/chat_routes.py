from fastapi import APIRouter
from app.schemas.chat_request import Chat_Request
from app.services.chat_service import run_chat

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/chat")
def chat_request(request: Chat_Request):
    return run_chat(request.session_id, request.message, request.top_k)

