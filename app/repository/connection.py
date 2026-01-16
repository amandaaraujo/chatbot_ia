import psycopg2
from app.config import DB_CONFIG    

def get_db_connection():
    if isinstance(DB_CONFIG, dict):
        return psycopg2.connect(**DB_CONFIG)
    return psycopg2.connect(DB_CONFIG)