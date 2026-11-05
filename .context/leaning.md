# Aprendizados e Padrões Estabelecidos

## Boas Práticas Identificadas

1. **Pydantic v2 ConfigDict:**
   - Para compatibilidade total com SQLAlchemy e evitar warnings de depreciação, utilizar sempre `model_config = ConfigDict(from_attributes=True)`.
2. **Timestamps Modernos no Python 3.11+:**
   - Evitar `datetime.utcnow()`. Utilizar sempre `lambda: datetime.now(timezone.utc)` para garantir compatibilidade com Python 3.12/3.13.
3. **SQLite em Memória para Testes Rápidos com FastAPI:**
   - Ao rodar testes de integração com `sqlite:///:memory:`, utilizar `StaticPool` e `connect_args={"check_same_thread": False}` para que as conexões concorrentes do `TestClient` enxerguem a mesma base criada no setup da fixture.
4. **Execução de Pytest a partir da Raiz:**
   - Em estruturas com pasta `backend/`, definir `$env:PYTHONPATH="backend"` no Windows PowerShell antes de rodar `pytest` para assegurar que imports absolutos do tipo `from app...` sejam resolvidos sem ambiguidade.
5. **Tailwind CSS v4 `@theme`:**
   - No Tailwind v4, tokens de cores e raios personalizados devem ser injetados dentro da diretiva `@theme` no CSS principal para ficarem disponíveis em classes utilitárias.
6. **Combinação de Textos no Testing Library:**
   - Quando um elemento contém múltiplos nós filhos (ex: texto intercalado com `span`), utilizar matchers com regex ou funções predicadas para evitar falhas falsas de correspondência exata.
7. **Padrão Spec-Kit e Ciclo de Convergência:**
   - Manter a rastreabilidade entre `spec.md`, `plan.md` e `tasks.md` permite que `/speckit-converge` certifique a integridade entre o código entregue e os requisitos antes do avanço para a próxima funcionalidade.
