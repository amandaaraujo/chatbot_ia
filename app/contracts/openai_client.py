from openai import OpenAIClient
import os

client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))

def embed_text(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def chat_response(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()