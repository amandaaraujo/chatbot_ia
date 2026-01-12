from typing import List
from pydantic import BaseModel


class ChatResponseDto(BaseModel):
    session_id: str
    response: str
    used_memories: List[str]