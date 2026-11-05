# Research & Architecture Decisions (As-Built): Candidate Profile

**Feature Branch**: `001-candidate-profile`  
**Date**: 2026-11-04  
**Status**: Implementado e Validado

## 1. Mapeamento da Implementação Existente

A funcionalidade foi inteiramente implementada e validada em conformidade com as especificações técnicas anteriores (`specs/01-candidate-profile.md`):

### Backend (`backend/app/`):
- **Modelos de Dados ORM (`app/models/entities.py`)**:
  - `CandidateProfileModel`: Tabela `candidate_profiles` com suporte a UUID v4, JSON para arrays (`target_roles`, `work_modes`) e relacionamentos com cascata (`cascade="all, delete-orphan"`).
  - `ExperienceModel`: Tabela `experiences` com `ForeignKey("candidate_profiles.id", ondelete="CASCADE")`.
  - `EducationModel`: Tabela `educations` com ordenação por `order_index`.
  - `SkillModel`: Tabela `skills` com suporte a enums `SkillCategory` (`TECHNICAL`, `SOFT_SKILL`, `LANGUAGE`).
- **Esquemas Pydantic (`app/models/profile.py`)**:
  - Modelos com validação estrita via `BaseModel`: `CandidateProfileCreate`, `CandidateProfileUpdate`, `CandidateProfileResponse`.
  - `@model_validator(mode="after")` em `ExperienceSchema` para validar consistência cronológica (`start_date <= end_date` e bloqueio de `end_date` em cargo atual).
- **Repositório Isolado (`app/repositories/profile_repository.py`)**:
  - `CandidateProfileRepository`: Métodos `get_first_profile()`, `create_profile()`, `update_profile()` e `delete_profile()`, encapsulando totalmente sessões SQLAlchemy e transações atômicas com `db.commit()` e `db.refresh()`.
- **Roteamento FastAPI (`app/api/profile.py`)**:
  - Endpoints RESTful:
    - `GET /api/v1/profile`
    - `PUT /api/v1/profile`
    - `DELETE /api/v1/profile` (status 204 No Content)
- **Suíte de Testes Pytest (`backend/tests/`)**:
  - `tests/unit/test_profile_schemas.py`: Validação de tipos e datas.
  - `tests/integration/test_profile_repository.py`: Ciclo de persistência no banco SQLite isolado de testes.
  - `tests/api/test_profile_api.py`: Testes com `TestClient` cobrindo o fluxo completo de requisições HTTP e códigos de status.

### Frontend (`frontend/src/`):
- **Componentes Atômicos de UI (`src/components/ui/`)**:
  - `Button.tsx`: Variantes `primary`, `secondary`, `ghost`, `danger` com tokens do Design System e acessibilidade de foco visível.
  - `Input.tsx`: Campo com suporte a `error`, `aria-describedby` e tema escuro `#181D25`.
  - `Badge.tsx`: Badges semânticos com variantes `neutral`, `brand`, `success`, `warning`, `danger`.
  - `Card.tsx`: Superfície `#181D25`, borda `#303947`, raio de 14px.
- **Tela de Perfil (`src/sections/Profile/ProfileSection.tsx`)**:
  - Interface estruturada em abas/blocos com suporte a edição de dados pessoais, contatos, experiências dinâmicas, formação, competências e editor de currículo-base bruto em Markdown.
- **Serviço de API (`src/services/profileService.ts`)**:
  - Cliente com funções tipadas `getProfile()`, `upsertProfile()`, `deleteProfile()`.
- **Tipos Estritos (`src/types/profile.ts`)**:
  - Interfaces TypeScript estritas espelhando os esquemas Pydantic sem uso de `any`.
- **Suíte de Testes Vitest (`src/tests/`)**:
  - `tests/ui/Button.test.tsx`, `tests/ui/Input.test.tsx`, `tests/ui/BadgeAndCard.test.tsx`, `tests/sections/ProfileSection.test.tsx`.

---

## 2. Decisões Arquiteturais Confirmadas no Código

1. **Repositório Isolado (Sem SQL nas rotas)**:
   - A camada de API em `app/api/profile.py` apenas delega para `CandidateProfileRepository`, garantindo que regras de consulta e mutação fiquem blindadas e isoladas.
2. **Atomicidade no Upsert**:
   - Quando o perfil é atualizado, o repositório sincroniza as entidades filhas de maneira atômica na mesma transação, descartando ou atualizando itens antigos conforme a coleção enviada.
3. **Preservação de Dados Brutos**:
   - O campo `base_resume_raw` armazena o texto Markdown original do usuário sem sanitizações mutiladoras, garantindo a integridade do currículo fonte.
4. **Isolamento de Testes**:
   - Os testes de backend utilizam banco de dados em memória (`sqlite:///:memory:`) injetado via fixtures no `get_db`, garantindo rapidez e zero efeito colateral no banco de desenvolvimento.
