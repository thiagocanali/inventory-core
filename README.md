# InventoryCore
API de estoque transacional para lojas de eletrônicos. Fase 02: bootstrap.

## Executar
Copie `.env.example` para `.env` e execute `docker compose up --build -d`.
Swagger: http://localhost:8000/docs. Health: `/health/live` e `/health/ready`.
O banco não é exposto no host pelo Compose. Para testes locais, configure um PostgreSQL de testes separado e `DATABASE_URL` correspondente. Instale `pip install -e '.[dev]'` e execute `ruff check .` e `pytest`.
O teste de readiness exige PostgreSQL real. As credenciais de exemplo são apenas para desenvolvimento.

## Escopo atual
Não há CRUD, autenticação ou migrations de domínio nesta fase. Veja `docs/architecture.md` e `ROADMAP.md`.
