from app.repository.connection import get_db_connection

with get_db_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id SERIAL PRIMARY KEY,
            session_id VARCHAR(255) NOT NULL,
            text TEXT NOT NULL
        );
    ''')
        conn.commit()