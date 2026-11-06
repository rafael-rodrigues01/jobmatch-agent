# Research & Technical Decisions: Correção do Erro de Carregamento do Perfil

**Feature**: `002-fix-profile-load-error`  
**Date**: 2026-11-06  

## Decision 1: Estratégia de Fallback Resiliente de Banco no Backend

- **Decision**: No módulo `backend/app/core/database.py`, implementar inicialização defensiva com fallback automático para SQLite local (`sqlite:///./jobmatch.db`) caso o PostgreSQL configurado na `DATABASE_URL` não esteja acessível ou a conexão inicial falhe.
- **Rationale**: 
  - O JobMatch Agent é uma aplicação desktop/local-first focada no usuário final. Exigir que o usuário mantenha um container Docker ou serviço de background do PostgreSQL rodando 100% do tempo causa erros de inicialização frequentes no desktop.
  - SQLAlchemy abstrai perfeitamente as operações ORM já definidas (`CandidateProfileModel`, `ExperienceModel`, etc.), permitindo que tanto PostgreSQL quanto SQLite usem o mesmo repositório e modelos sem alteração de lógica.
  - Se `DATABASE_URL` estiver explicitamente definida e conectável, o PostgreSQL continua sendo a prioridade. Se a conexão falhar (ex: `OperationalError: Connection refused`), o engine faz fallback transparente para SQLite local e registra aviso nos logs.
- **Alternatives considered**:
  - *Exigir obrigatoriamente PostgreSQL*: Rejeitado porque gera falha imediata na primeira execução da aplicação na máquina do usuário quando o serviço do PostgreSQL estiver parado.
  - *Não subir o backend se o banco falhar*: Rejeitado porque quebra o princípio de resiliência e a experiência local-first.

## Decision 2: Feedback de Estado e Ação de Retry no Frontend

- **Decision**: 
  1. No `frontend/src/services/profileService.ts`, capturar falhas de rede (`TypeError: Failed to fetch` ou status 503/500) e encapsular erros com mensagem descritiva indicando se foi falha de conexão com a API local.
  2. No `frontend/src/sections/Profile/ProfileSection.tsx`, criar um estado específico de status de conexão (`api_unavailable`), exibindo um banner informativo semântico (Design System: cor `#F2B85B` warning / `#FF727F` danger) explicando que o serviço local da API em `http://localhost:8000` está inalcançável e oferecendo um botão acessível **"Tentar novamente"** (`Button` com variante `secondary` ou `primary`).
- **Rationale**:
  - Evita o alerta vermelho seco e estático "Não foi possível carregar os dados do perfil.", guiando o usuário de maneira humana e transparente sobre como proceder (ex.: verificar se o backend está rodando).
  - O botão "Tentar novamente" recarrega o estado assíncrono via `loadData()` sem forçar o usuário a dar refresh na página ou perder eventuais alterações.
- **Alternatives considered**:
  - *Polling automático infinito*: Rejeitado por consumir CPU e inundar o console com erros enquanto o usuário ainda não subiu o backend.
  - *Modal bloqueante*: Rejeitado porque bloqueia a tela; um banner com retry respeita a densidade e o controle do usuário.

## Decision 3: Preservação de Dados em Falha de Submissão

- **Decision**: Garantir que, se o usuário tentar salvar o perfil e o backend estiver offline, os dados digitados permaneçam 100% no formulário, alterando apenas o status de erro para "Serviço indisponível no momento. Seus dados continuam no formulário.".
- **Rationale**: Respeita o Princípio 1 do AGENTS.md e PRD (human-in-the-loop, proteção e controle de dados).

