# Progresso do Projeto

## Especificações Concluídas
- [x] **01 - Perfil do Candidato e Currículo-Base** (`specs/01-candidate-profile.md`)
  - Schemas Pydantic v2 com validação estrita de integridade
  - Repositório SQLAlchemy e persistência relacional com cascading
  - Endpoints RESTful FastAPI (`GET`, `PUT`, `DELETE /api/v1/profile`)
  - Tokens e componentes base do Design System (`Button`, `Input`, `Badge`, `Card`)
  - Tela de edição e visualização de perfil (`ProfileSection`) com feedback
  - 13 testes unitários/integração no backend (Pytest)
  - 12 testes no frontend (Vitest + RTL)
  - Build de produção TypeScript sem erros

## Próximas Especificações (Roadmap PRD)
- [ ] **02 - Coleta, Normalização e Deduplicação de Vagas** (Fase 2 do PRD: RF-04, RF-05, RF-10)
- [ ] **03 - Motor de Análise de Aderência com IA** (Fase 3 do PRD: RF-06)
- [ ] **04 - Geração e Exportação de Currículo Direcionado** (Fase 4 do PRD: RF-07, RF-08)
- [ ] **05 - Agendador e Automação Local** (Fase 5/6 do PRD: RF-03, RF-09, RF-11)
