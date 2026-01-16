from app.repository.chat_repository import add_memory, list_memories
from app.integrations.openai_client import chat_response
from uuid import uuid4

def ensure_session_id(session_id: str | None) -> str:
    return session_id if session_id else str(uuid4())

def build_context(memories: list[str]) -> str:
    if not memories:
        return "(sem memória)"
    return "\n".join(f"- {m}" for m in memories)

def run_chat(session_id: str | None, message: str, top_k: int = 5) -> dict:
    sid = ensure_session_id(session_id)

    add_memory(sid, f"[USER] {message}")

    memories = list_memories(sid, limit=top_k)

    context = build_context(memories[::-1]) 

    prompt = (
        "Você é um assistente útil.\n"
        "Use o contexto abaixo se for relevante.\n\n"
        f"CONTEXTO:\n{context}\n\n"
        f"USUÁRIO: {message}\n"
        "ASSISTENTE:"
    )

    reply = chat_response(prompt)

    add_memory(sid, f"[ASSISTANT] {reply}")

    return {
        "session_id": sid,
        "reply": reply,
        "memories": memories[::-1],
    }