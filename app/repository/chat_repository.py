from app.repository.connection import get_db_connection

def add_memory(session_id: str, text: str) -> None:
    with get_db_connection() as connection:
        with connection.cursor() as cur:
            cur.execute(
                "INSERT INTO memories (session_id, text) VALUES (%s, %s);",
                (session_id, text),
            )

def list_memories(session_id: str, limit: int = 5) -> list[str]:
    with get_db_connection() as connection:
        with connection.cursor() as cur:
            cur.execute(
                "SELECT text FROM memories WHERE session_id = %s ORDER BY id DESC LIMIT %s;",
                (session_id, limit),
            )
            rows = cur.fetchall()
    return [row[0] for row in rows]