# Aprendizados e Padrões Estabelecidos

## Boas Práticas Identificadas

1. **Pydantic v2 ConfigDict:**
   - Para compatibilidade total com SQLAlchemy e evitar warnings de depreciação, utilizar sempre `model_config = ConfigDict(from_attributes=True)`.
2. **Timestamps Modernos no Python 3.11+:**
   - Evitar `datetime.utcnow()`. Utilizar sempre `lambda: datetime.now(timezone.utc)` para garantir compatibilidade com Python 3.12/3.13.
3. **SQLite em Memória para Testes Rápidos com FastAPI:**
   - Ao rodar testes de integração com `sqlite:///:memory:`, utilizar `StaticPool` e `connect_args={"check_same_thread": False}` para que as conexões concorrentes do `TestClient` enxerguem a mesma base criada no setup da fixture.
4. **Fallback Local-First para Desktop:**
   - Em aplicações com proposta desktop/local-first, implementar fallback de persistência transparente (PostgreSQL como primário quando acessível, e SQLite em arquivo local caso o serviço não esteja rodando). Isso evita crashes de inicialização como `OperationalError: Connection refused`.
5. **Resolução de `pythonpath` via `pytest.ini`:**
   - Incluir `pytest.ini` com `pythonpath = .` dentro de `backend/` para garantir que o comando `pytest` funcione diretamente tanto de dentro da pasta `backend/` quanto nos scripts de CI sem depender de flags manuais de ambiente.
6. **Erros de Rede Amigáveis e Ação de Retry:**
   - Nunca exibir alertas vermelhos estáticos genéricos quando o erro for decorrente de indisponibilidade de backend. Capturar `TypeError: Failed to fetch`, prover mensagem honesta orientando o usuário a verificar o serviço e disponibilizar um botão de **"Tentar novamente"** sem forçar F5 no navegador.
7. **Combinação de Textos no Testing Library:**
   - Quando um elemento contém múltiplos nós filhos (ex: texto intercalado com `span`), utilizar matchers com regex ou funções predicadas para evitar falhas falsas de correspondência exata.
8. **Padrão Spec-Kit e Ciclo de Convergência:**
   - Manter a rastreabilidade entre `spec.md`, `plan.md` e `tasks.md` permite que `/speckit-converge` certifique a integridade entre o código entregue e os requisitos antes do avanço para a próxima funcionalidade.
