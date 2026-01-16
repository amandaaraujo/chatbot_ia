from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key = OPENAI_API_KEY)

def chat_response(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY não está definida no ambiente (.env / Docker / Kubernetes).")