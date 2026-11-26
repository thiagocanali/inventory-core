# Decisões arquiteturais
- Monólito modular em camadas: rotas, controllers, services, repositories, models e schemas serão introduzidos quando necessários.
- SQLAlchemy síncrono e endpoints síncronos para operações de banco; transações pertencem aos services, nunca aos repositories.
- PostgreSQL READ COMMITTED, UPDATE condicional com RETURNING e CHECK de saldo não negativo. Pedidos com vários itens bloqueiam produtos em ordem estável. Cancelamentos bloqueiam o pedido antes do estorno.
- Pedido, itens, estoque e histórico devem compartilhar a mesma transação. Testes de concorrência usarão sessões independentes e PostgreSQL real.
- Liveness não consulta banco; readiness consulta banco e retorna 503 em indisponibilidade.
- Docker sem root, banco sem porta pública, CI com PostgreSQL. Sem deploy automático.
- Dependências com intervalos de versão; lockfile e revisão de segurança ainda pendentes.
