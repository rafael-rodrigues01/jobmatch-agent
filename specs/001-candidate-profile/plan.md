# Implementation Plan: Candidate Profile & Base Resume Management (As-Built)

**Branch**: `001-candidate-profile` | **Date**: 2026-11-04 | **Spec**: [specs/001-candidate-profile/spec.md](spec.md)

**Input**: Feature specification retroativa mapeando e documentando a implementação concluída em `backend/` e `frontend/`.

## Summary

O módulo de Perfil do Candidato e Currículo-Base constitui a **única fonte da verdade** para o JobMatch Agent, respeitando os princípios de *Human-in-the-Loop* e *Zero Alucinação*. A implementação encontra-se concluída, testada e validada em sua totalidade no código-fonte, composta por API FastAPI com repositório isolado SQLAlchemy no PostgreSQL/SQLite e interface em React 19 + TypeScript (strict mode) com Tailwind CSS v4.

## Technical Context

**Language/Version**: Python 3.13 / Node.js 20+ (TypeScript 5.x em modo strict)  
**Primary Dependencies**: FastAPI 0.115+, Pydantic v2, SQLAlchemy 2.0+, React 19, Tailwind CSS v4, Lucide React  
**Storage**: PostgreSQL (em produção/desenvolvimento) / SQLite in-memory (em testes automatizados Pytest)  
**Testing**: Pytest (13 testes passando em verde), Vitest + React Testing Library (12 testes passando em verde)  
**Target Platform**: Desktop local / Local-first Web App  
**Project Type**: Web Application desacoplada (`backend` API + `frontend` SPA)  
**Performance Goals**: Tempo de resposta de persistência e leitura < 100ms localmente  
**Constraints**: Zero mutação ou inferência de dados do usuário; validação temporal em Pydantic; WCAG AA com navegação por teclado; Zero `any`  
**Scale/Scope**: Perfil de usuário único no MVP local  

## Constitution Check

*GATE: Post-Design & Implementation Verification.*

- [x] **Princípio 1 (Human-in-the-Loop & Governança)**: O usuário tem controle soberano sobre os dados cadastrados e exclusão total do perfil (`DELETE /api/v1/profile` retornando 204).
- [x] **Princípio 2 (Zero Alucinação)**: O perfil cadastrado é tratado como verdade absoluta; nenhuma IA ou serviço background altera dados sem intervenção do usuário.
- [x] **Princípio 3 (Test-First & Tríade Pré-CI/CD)**:
  - Lint/TypeScript: `npm run build` executa `tsc -b` sem erros.
  - Testes Unitários/Integração: `npm test -- --run` (12 testes OK) e `pytest backend/tests` (13 testes OK).
- [x] **Princípio 4 (Repositório Isolado)**: Toda persistência está centralizada em `backend/app/repositories/profile_repository.py`. Nenhuma consulta SQL presente em controladores.
- [x] **Princípio 5 (Design System & Acessibilidade)**: Componentes atômicos utilizam os tokens exatos do `DESIGN-SYSTEM.md` (`#101318` canvas, `#181D25` surface, `#202733` elevated, `#303947` border, `#6C8CFF` brand).

## Project Structure (Estado Atual do Código)

```text
backend/
├── app/
│   ├── api/
│   │   └── profile.py                     # Rotas GET, PUT e DELETE /api/v1/profile
│   ├── core/
│   │   └── database.py                    # Configuração de engine e get_db session
│   ├── models/
│   │   ├── entities.py                    # Classes ORM: CandidateProfileModel, ExperienceModel, EducationModel, SkillModel
│   │   └── profile.py                     # Pydantic Schemas com validadores de datas e enums
│   ├── repositories/
│   │   └── profile_repository.py          # CandidateProfileRepository com operações atômicas
│   └── main.py                            # Ponto de entrada FastAPI com inclusão do router de perfil
└── tests/
    ├── api/
    │   └── test_profile_api.py            # Testes com TestClient da API HTTP
    ├── integration/
    │   └── test_profile_repository.py     # Testes de operações no repositório com banco em memória
    └── unit/
        └── test_profile_schemas.py        # Testes de validação Pydantic de datas e campos obrigatórios

frontend/
├── src/
│   ├── components/
│   │   └── ui/
│   │       ├── Button.tsx                 # Botão acessível com variantes do Design System
│   │       ├── Input.tsx                  # Input com suporte a erros e aria-describedby
│   │       ├── Badge.tsx                  # Badges semânticos de status
│   │       └── Card.tsx                   # Card de superfície elevada
│   ├── sections/
│   │   └── Profile/
│   │       └── ProfileSection.tsx         # Formulário unificado de gestão do perfil e currículo bruto
│   ├── services/
│   │   └── profileService.ts              # Cliente HTTP tipado (getProfile, upsertProfile, deleteProfile)
│   ├── types/
│   │   └── profile.ts                     # Interfaces estritas TypeScript (sem `any`)
│   └── tests/
│       ├── sections/
│       │   └── ProfileSection.test.tsx    # Testes RTL da tela de perfil
│       └── ui/
│           ├── Button.test.tsx
│           ├── Input.test.tsx
│           └── BadgeAndCard.test.tsx
```

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| *Nenhuma violação identificada* | Arquitetura 100% conforme as diretrizes do `AGENTS.md` | N/A |
