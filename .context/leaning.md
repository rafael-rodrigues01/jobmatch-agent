# Aprendizados e Padrões Estabelecidos

## Boas Práticas Identificadas
1. **Pydantic v2 ConfigDict:**
   - Para compatibilidade total com SQLAlchemy e evitar warnings de depreciação, utilizar sempre `model_config = ConfigDict(from_attributes=True)`.
2. **Timestamps Modernos no Python 3.11+:**
   - Evitar `datetime.utcnow()`. Utilizar sempre `lambda: datetime.now(timezone.utc)` para garantir compatibilidade com Python 3.12/3.13.
3. **SQLite em Memória para Testes Rápidos com FastAPI:**
   - Ao rodar testes de integração com `sqlite:///:memory:`, utilizar `StaticPool` e `connect_args={"check_same_thread": False}` para que as conexões concorrentes do `TestClient` enxerguem a mesma base criada no setup da fixture.
4. **Tailwind CSS v4 `@theme`:**
   - No Tailwind v4, tokens de cores e raios personalizados devem ser injetados dentro da diretiva `@theme` no CSS principal para ficarem disponíveis em classes utilitárias.
5. **Combinação de Textos no Testing Library:**
   - Quando um elemento contém múltiplos nós filhos (ex: texto intercalado com `span`), utilizar matchers com regex ou funções predicadas para evitar falhas falsas de correspondência exata.
