from db import get_connection
from openai_client import chat_response, embed_text

def save_memory(session_id: str, text: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO memories (session_id, text) VALUES (?, ?)',
        (session_id, text)
    )

def load_memories(session_id: str, top_k: int):
    with get_connection() as conn:
        rows = conn.execute(
            'SELECT text FROM memories WHERE session_id = ? ORDER BY created_at DESC LIMIT ?',
            (session_id, top_k)
        ).fetchall()
        return [r[0] for r in rows]

def chat_service(session_id: str | None, message: str, top_k: int):
    if not session_id:
        session_id = "S-" + message[:6]

    memories = load_memories(session_id, top_k)

    context = "\n".join(f"- {mem}" for mem in memories) if memories else "(sem memória)." 
    
    prompt = f"Considere as seguintes memórias do usuário:\n{context}\n\nUsuário: {message}\n"

    response = chat_response(prompt)

    save_memory(session_id, message)
    save_memory(session_id, response)   

    return session_id, response, memories