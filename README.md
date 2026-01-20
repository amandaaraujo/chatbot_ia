___ Chatbot com Memória Persistente (Mock Inteligente + Arquitetura Pronta para RAG) ___

Este projeto implementa um chatbot stateful com memória persistente, desenvolvido em Python + FastAPI, com PostgreSQL, Docker e Kubernetes (kind).

O sistema foi projetado para demonstrar boas práticas de arquitetura backend, separação de responsabilidades e preparação para evoluir para RAG (Retrieval-Augmented Generation), mesmo operando atualmente em modo mock inteligente, sem dependência de serviços externos.

- Objetivo do Projeto

Demonstrar, de forma prática, habilidades em:

Backend moderno com Python
APIs REST com FastAPI
Persistência e estado por sessão
Arquitetura limpa (service / repository / integrations)
Containers (Docker)
Orquestração (Kubernetes)
Estratégias de fallback (mock vs IA real)
Observabilidade básica (health check, logs)
O projeto foi pensado para ser realista, executável localmente e fácil de evoluir.

- O que este chatbot faz?

Conversa via endpoint /chat
Mantém estado por sessão (session_id)
Persiste histórico no PostgreSQL
Recupera memórias recentes (top_k)
Responde usando: Mock, OpenAI (opcional) - desativado por padrão e funciona sem dependência externa (modo demonstração)

- Arquitetura

app/
├── api/            # Rotas FastAPI
│   └── chat_routes.py
├── services/       # Regras de negócio
│   └── chat_service.py
├── repository/     # Persistência (Postgres)
│   └── chat_repository.py
├── integrations/   # Integrações externas
│   └── openai_client.py
├── config.py       # Configurações por ambiente
└── main.py         # Bootstrap da aplicação

- Princípios aplicados

Separação de responsabilidades
Código testável e extensível
Integrações desacopladas
Fácil troca entre mock ↔ IA real

- Persistência

Banco: PostgreSQL

Armazena: session_id, mensagens do usuário, histórico conversacional e recupera memórias recentes para cada interação

- Docker

A aplicação é empacotada em um container Docker: docker build -t chatbot-api:1.0 .
Python 3.12
Dependências isoladas
Pronto para rodar localmente ou em cluster

- Kubernetes (kind)

O projeto roda em um cluster Kubernetes local (kind), com:

Deployment da API
Deployment do Postgres
Service interno
Probes de: liveness, readiness

- Executar localmente

kubectl apply -f k8s/
kubectl port-forward svc/chatbot-api-svc 8000:80


Swagger:

http://127.0.0.1:8000/docs

- Configuração por Ambiente

Controlado via variáveis de ambiente:

Variável	Descrição
USE_OPENAI	Ativa/desativa IA real
OPENAI_API_KEY	Chave da OpenAI (opcional)
DB_HOST	Host do Postgres
DB_NAME	Nome do banco
DB_USER	Usuário
DB_PASSWORD	Senha

🔒 Por padrão: USE_OPENAI=false
➡️ O sistema funciona 100% em modo mock.

- Observação Importante

Este projeto foi intencionalmente desenvolvido sem dependência obrigatória de IA externa, garantindo:

execução local simples
previsibilidade de custos
facilidade de avaliação técnica

- Autora

Projeto desenvolvido como demonstração prática de backend moderno, arquitetura limpa e preparação para sistemas de IA aplicados.