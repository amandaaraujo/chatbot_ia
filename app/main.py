import time
import psycopg2
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.repository.connection import init_db
from app.api.chat_routes import router as chat_routes


def init_db_with_retry(retries: int = 10, delay: float = 2.0):
    for _ in range(retries):
        try:
            init_db()
            return
        except psycopg2.OperationalError:
            time.sleep(delay)
    raise RuntimeError("DB não ficou disponível a tempo.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db_with_retry()
    yield

app = FastAPI(lifespan = lifespan)
app.include_router(chat_routes)
