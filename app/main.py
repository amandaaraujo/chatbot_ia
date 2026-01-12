from fastapi import FastAPI
from pydantic import BaseModel
import os
import psycopg2

app = FastAPI()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "chatbot"),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "app")
    )
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id SERIAL PRIMARY KEY,
            session_id VARCHAR(255) NOT NULL,
            text TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.on_event("startup")
def startup_event():
    init_db()

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None
    top_k: int = 5

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    conn = get_db_connection()
    cursor = conn.cursor()  
    cursor.execute(
        "INSERT INTO memories (session_id, text) VALUES (%s, %s);",
        (request.session_id, request.message)
    )
    conn.commit()
    cursor.execute(
        "SELECT text FROM memories WHERE session_id = %s ORDER BY id DESC LIMIT 5;",
        (request.session_id)
    )

    memories = [r[0] for r in cursor.fetchall()]

    cursor.close()
    conn.close()

    return {"reply": f"Guardei sua mensagem. Últimas memórias: {memories[::-1]}"}

# user = input('Olá! Digite seu nome para começar a conversar.')
# message = input(f'{user}, como posso te ajudar hoje?')

# def custom_chat():
#     print("Olá! Digite seu nome para começar a conversar.")
