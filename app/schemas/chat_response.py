from typing import List
from pydantic import BaseModel


class Chat_Response(BaseModel):
    session_id: str
    response: str
    used_memories: List[str]