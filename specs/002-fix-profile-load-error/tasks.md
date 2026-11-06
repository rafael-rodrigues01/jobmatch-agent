---
description: "Task list for Correção do Erro de Carregamento do Perfil no Frontend"
---

# Tasks: Correção do Erro de Carregamento do Perfil no Frontend

**Input**: Design documents from `/specs/002-fix-profile-load-error/` (`spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/profile-health-api.yaml`, `quickstart.md`)  
**Prerequisites**: plan.md (concluído), spec.md (concluído), research.md (concluído), data-model.md (concluído), contracts/ (concluído)  
**Tests**: Testes automatizados incluídos conforme TDD e diretrizes do `AGENTS.md` (Pytest para backend, Vitest + RTL para frontend).  
**Status**: Todas as 16 tarefas implementadas, validadas e 100% dos testes passando em verde.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Tarefa executável em paralelo (arquivos distintos, sem dependência bloqueante)
- **[Story]**: Mapeamento para história de usuário correspondente (`[US1]`, `[US2]`)
- Caminhos exatos para backend em `backend/` e frontend em `frontend/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Garantir que as configurações de ambiente e testes estejam alinhadas

- [x] T001 [P] Criar arquivo de exemplo de ambiente `backend/.env.example` documentando as variáveis `DATABASE_URL` e modo de fallback
- [x] T002 [P] Atualizar arquivo `backend/requirements.txt` incluindo explicitamente `uvicorn>=0.30.0` para paridade de ambiente local

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Estrutura base de persistência defensiva e status da API

- [x] T003 Implementar inicialização com fallback automático para SQLite (`sqlite:///./jobmatch.db`) caso PostgreSQL não conecte em `backend/app/core/database.py`
- [x] T004 Atualizar endpoint de verificação em `backend/app/main.py` para reportar status e tipo de banco ativo em `/health`

**Checkpoint**: Backend inicializa resilientemente com SQLite caso o PostgreSQL esteja parado.

---

## Phase 3: User Story 1 - Diagnóstico Claro e Ação Diante da Indisponibilidade do Backend/Banco (Priority: P1) 🎯 MVP

**Goal**: Exibir banner explicativo contextualizado com botão "Tentar novamente" quando o backend estiver inalcançável, substituindo a mensagem genérica em vermelho.

**Independent Test**: Iniciar apenas o frontend (sem backend) e verificar que a interface exibe banner informativo claro com botão "Tentar novamente", sem travar a tela e permitindo nova busca assim que a API responder.

### Tests for User Story 1

- [x] T005 [P] [US1] Criar testes unitários para tratamento de erro offline e de rede em `frontend/src/tests/services/profileService.test.ts`
- [x] T006 [P] [US1] Criar teste RTL simulando backend offline e clique de recuperação em "Tentar novamente" em `frontend/src/tests/sections/ProfileSection.test.tsx`

### Implementation for User Story 1

- [x] T007 [P] [US1] Atualizar `frontend/src/services/profileService.ts` para capturar exceções de rede (`TypeError: Failed to fetch`) e lançar erros tipados identificando serviço offline
- [x] T008 [US1] Implementar no componente `frontend/src/sections/Profile/ProfileSection.tsx` o banner contextualizado do Design System com estado `isOffline` e botão "Tentar novamente"
- [x] T009 [US1] Garantir preservação total de valores digitados no formulário durante falhas de conexão em `frontend/src/sections/Profile/ProfileSection.tsx`

**Checkpoint**: User Story 1 funcional de forma independente. O usuário tem feedback transparente e controle de reconexão.

---

## Phase 4: User Story 2 - Resiliência e Fallback Local de Persistência (Priority: P2)

**Goal**: Garantir que o backend suba localmente sem erros de `Connection refused` no PostgreSQL, usando SQLite e criando tabelas necessárias sob demanda.

**Independent Test**: Executar teste de integração do banco simulando falha do PostgreSQL e verificando criação automática do schema no SQLite.

### Tests for User Story 2

- [x] T010 [P] [US2] Criar teste de integração para o fallback de banco de dados em `backend/tests/integration/test_database_fallback.py`

### Implementation for User Story 2

- [x] T011 [US2] Adicionar inicialização idempotente de tabelas (`Base.metadata.create_all(bind=engine)`) no startup de `backend/app/main.py` quando em fallback local
- [x] T012 [US2] Adicionar log estruturado sanitizado indicando o banco de dados utilizado (PostgreSQL vs SQLite local) em `backend/app/core/database.py`

**Checkpoint**: User Story 2 validada. A aplicação funciona out-of-the-box localmente sem dependência obrigatória do PostgreSQL.

---

## Phase 5: Polish & Quality Assurance

**Purpose**: Validação da tríade de qualidade exigida pelo `AGENTS.md` e GitHub Actions

- [x] T013 [P] Executar testes unitários e de integração do backend via Pytest (`cd backend; pytest`)
- [x] T014 [P] Executar testes do frontend via Vitest (`cd frontend; npm test -- --run`)
- [x] T015 Compilar frontend com `npm run build` garantindo zero erros TypeScript (`tsc -b`)
- [x] T016 Executar validação manual ponta a ponta conforme cenários de `specs/002-fix-profile-load-error/quickstart.md`
