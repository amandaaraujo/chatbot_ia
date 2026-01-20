import os
from openai import OpenAI, OpenAIError, RateLimitError
from app.config import OPENAI_API_KEY

_client: OpenAI | None = None

def _mock_response(_: str) -> str:
    return "Modo demo ativo: esta é resposta simulada (sem OpenAI) para teste do sistema." 

def _get_client() -> OpenAI:
    global _client
    api_key = os.getenv("OPENAI_API_KEY")
    if _client is None:
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY não configurada")
        _client = OpenAI(api_key=api_key)
    return _client

def chat_response(prompt: str) -> str:
    use_openai = os.getenv("USE_OPENAI", "false").lower() == "true"
    if not use_openai:
        return _mock_response(prompt)

    try:
        client = _get_client()
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return res.choices[0].message.content.strip()

    except RateLimitError:
        return "IA indisponível no momento (limite/quota atingido)."

    except OpenAIError:
        return "Erro ao gerar resposta com IA."
    