# Contexto Ativo

## Foco Atual
- Finalização da **Fase 1 (Fundação & Perfil do Candidato)** e preparação para a **Fase 2 (Vagas: Coleta, Normalização e Deduplicação)**.

## Últimas Ações Realizadas
- Implementação completa da especificação técnica `specs/01-candidate-profile.md` em fluxo TDD rigoroso.
- Criação dos schemas Pydantic v2, modelos ORM SQLAlchemy e repositório isolado em `backend/`.
- Criação e validação dos endpoints RESTful (`GET`, `PUT`, `DELETE /api/v1/profile`) com 13 testes em Pytest.
- Setup do frontend com React 19, Vite, TypeScript estrito, Tailwind CSS v4 e Vitest.
- Criação dos componentes atômicos do Design System (`Button`, `Input`, `Badge`, `Card`) e da tela `ProfileSection` com 12 testes passando.
- Documentação dos Changelogs em `backend/changelog.md` e `frontend/changelog.md`.

## Próximos Passos Imediatos
- Iniciar o planejamento da **Fase 2 do PRD (Vagas)**:
  - Elaboração da especificação `specs/02-job-ingestion-dedup.md`.
  - Mapeamento das regras de normalização de URLs e deduplicação (RF-05).
  - Modelagem de dados para vagas (`Job`) e histórico de atividades (`ApplicationActivity`).
