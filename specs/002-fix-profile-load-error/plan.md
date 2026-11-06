# Implementation Plan: Correção do Erro de Carregamento do Perfil no Frontend

**Branch**: `002-fix-profile-load-error` | **Date**: 2026-11-06 | **Spec**: [specs/002-fix-profile-load-error/spec.md](spec.md)

**Input**: Feature specification de `specs/002-fix-profile-load-error/spec.md` para eliminar falhas de carregamento e prover diagnóstico e recuperação clara de indisponibilidade de backend.

## Summary

O objetivo desta feature é tornar a experiência de inicialização do JobMatch Agent resiliente e transparente. Quando o usuário abre o frontend sem o backend rodando, em vez de exibir um erro vermelho seco e genérico ("Não foi possível carregar os dados do perfil."), a interface apresentará um banner explicativo com indicação de que o serviço local está inalcançável e um botão interativo de **"Tentar novamente"** (sem precisar de recarga de página). No backend, será adicionado um fallback transparente para SQLite local quando o PostgreSQL não estiver acessível, garantindo que o backend suba sem erros de conexão recusada mesmo em ambientes sem PostgreSQL configurado.

## Technical Context

**Language/Version**: Python 3.13 / TypeScript 5.7+ (React 19)  
**Primary Dependencies**: FastAPI, SQLAlchemy, Pydantic, React 19, Lucide React, Tailwind CSS v4  
**Storage**: PostgreSQL (primário) / SQLite local `jobmatch.db` (fallback defensivo)  
**Testing**: Pytest (backend), Vitest + React Testing Library (frontend)  
**Target Platform**: Desktop / Local-first Web App (Windows)  
**Project Type**: Web Application desacoplada (`backend` FastAPI + `frontend` Vite/React)  
**Performance Goals**: Recuperação do estado de erro em < 2s após restabelecimento do serviço  
**Constraints**: Não perder dados digitados pelo usuário em caso de queda de rede; WCAG AA com navegação por teclado e botões acessíveis; Zero `any` no TypeScript.  
**Scale/Scope**: Ambiente desktop local-first para usuário individual.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Princípio 1 (Human-in-the-Loop & Governança)**: O usuário tem clareza sobre o estado do sistema e controle de retry sem ações automáticas obscuras.
- [x] **Princípio 2 (Zero Alucinação)**: Nenhuma mutação ou geração fictícia de dados. Os dados digitados no formulário são mantidos intactos caso a requisição falhe.
- [x] **Princípio 3 (Tríade Pré-CI/CD e TDD)**: Todas as alterações em serviços e componentes acompanham testes unitários correspondentes no Pytest e Vitest.
- [x] **Princípio 4 (Repositório Isolado)**: Toda a lógica de fallback de persistência permanece isolada na camada de infraestrutura (`backend/app/core/database.py`), mantendo os repositórios inalterados.
- [x] **Princípio 5 (Design System & Tokens)**: Mensagens de erro e alerta utilizam tokens `#FF727F` (danger), `#F2B85B` (warning) e botão estilizado com raio de 10px e foco visível.

## Project Structure

### Documentation (this feature)

```text
specs/002-fix-profile-load-error/
├── plan.md              # Este arquivo
├── research.md          # Decisões de fallback e tratamento de erros de rede
├── data-model.md        # Transições de estado do frontend e configuração de banco
├── quickstart.md        # Roteiro de validação de cenários de queda e recuperação
├── contracts/
│   └── profile-health-api.yaml # Contrato de status e respostas de erro
└── checklists/
    └── requirements.md  # Checklist de qualidade da especificação
```

### Source Code Impacted

```text
backend/
├── app/
│   ├── core/
│   │   └── database.py          # Fallback defensivo para SQLite se PostgreSQL falhar
│   └── main.py                  # Endpoint /health com indicação do banco conectado
└── tests/
    └── integration/
        └── test_database_fallback.py # Teste do fallback automático de conexão

frontend/
├── src/
│   ├── services/
│   │   └── profileService.ts    # Tratamento detalhado de erro (TypeError / network offline)
│   ├── sections/
│   │   └── Profile/
│   │       └── ProfileSection.tsx # Banner amigável de serviço indisponível com botão Retry
│   └── tests/
│       └── sections/
│           └── ProfileSection.test.tsx # Teste RTL de exibição de erro offline e ação de retry
```

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| *Nenhuma violação* | O fallback para SQLite e o botão de retry usam as ferramentas já presentes no projeto | N/A |
