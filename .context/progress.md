# Progresso do Projeto

## Especificações Concluídas
- [x] **001 - Perfil do Candidato e Currículo-Base** (`specs/001-candidate-profile/`)
  - **Status de Convergência**: 100% OK (Validado via `/speckit-converge`).
  - **Backend (Pytest)**: 13 testes passando (100% verde) cobrindo schemas Pydantic v2, repositório SQLAlchemy e rotas FastAPI (`GET`, `PUT`, `DELETE /api/v1/profile`).
  - **Frontend (Vitest + RTL)**: 12 testes passando (100% verde) cobrindo componentes atômicos (`Button`, `Input`, `Badge`, `Card`) e a tela `ProfileSection`.
  - **Build de Produção**: `tsc -b` executado sem erros com tipagem estrita (zero `any`) e bundle do Vite compilado com sucesso.
  - **Governança & Integridade**: Regras de *Zero Alucinação* e *Human-in-the-Loop* integralmente atendidas; exclusão definitiva em cascata funcional.
  - **CI Pipeline**: GitHub Actions configurado e validado em paralelo para Frontend (Node 20) e Backend (Python 3.11).

- [x] **002 - Correção do Erro de Carregamento e Resiliência Local** (`specs/002-fix-profile-load-error/`)
  - **Frontend**: Tratamento de exceção de rede (`ApiConnectionError`), exibição de alerta contextualizado no Design System com botão de recarga interativa ("Tentar novamente") e preservação de campos.
  - **Backend**: Fallback automático e transparente para SQLite local (`sqlite:///./jobmatch.db`) caso o servidor PostgreSQL não esteja rodando, permitindo uso desktop local-first sem impedimentos de infraestrutura.
  - **Qualidade**: 14 testes backend e 15 testes frontend passando em verde; build de produção 100% limpo.

## Próximas Especificações (Roadmap PRD)
- [ ] **003 - Coleta, Normalização e Deduplicação de Vagas** (Fase 2 do PRD: RF-04, RF-05, RF-10)
- [ ] **004 - Motor de Análise de Aderência com IA** (Fase 3 do PRD: RF-06)
- [ ] **005 - Geração e Exportação de Currículo Direcionado** (Fase 4 do PRD: RF-07, RF-08)
- [ ] **006 - Agendador e Automação Local** (Fase 5/6 do PRD: RF-03, RF-09, RF-11)
