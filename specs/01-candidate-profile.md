# Especificação Técnica: 01 - Perfil do Candidato e Currículo-Base

**Status:** Concluído e Validado (100% Cobertura de Testes)  
**Versão:** 1.0.0  
**Data:** 2026-11-03  
**Módulos Impactados:** `backend` (FastAPI / PostgreSQL), `frontend` (React / Tailwind)  
**Requisitos Relacionados:** RF-01, RF-02, RF-12 do PRD.md

---

## 1. Visão Geral e Objetivos

O módulo de Perfil do Candidato constitui a **única fonte da verdade** para todo o JobMatch Agent. É a base que sustenta a comparação de requisitos com vagas e a geração de currículos direcionados, proibindo categoricamente qualquer inferência ou alucinação de dados que não estejam formalmente cadastrados.

### Objetivos Específicos
1. Permitir visualização, criação e atualização integral do perfil do candidato e de suas entidades filhas (experiências, formação acadêmica, competências técnicas/comportamentais, idiomas e preferências).
2. Manter e versionar o conteúdo bruto do currículo-base em texto/Markdown de forma intocada (sem mutação automática).
3. Expor endpoints RESTful no backend Python com validação rigorosa via Pydantic e persistência no PostgreSQL via repositórios isolados.
4. Fornecer interface em React 19 + TypeScript (strict mode) alinhada ao Design System (tokens escuros, WCAG AA, componentes atômicos).

---

## 2. Arquitetura de Dados e Esquemas

### 2.1 Modelo Conceitual (PostgreSQL / SQLAlchemy)

- **`candidate_profiles`**:
  - `id`: UUID (PK, default uuidv4)
  - `full_name`: VARCHAR(255), Not Null
  - `headline`: VARCHAR(255), Nullable (ex: "Desenvolvedor Backend Sênior")
  - `summary`: TEXT, Nullable (resumo profissional)
  - `email`: VARCHAR(255), Nullable
  - `phone`: VARCHAR(50), Nullable
  - `location`: VARCHAR(255), Nullable (cidade/UF/país)
  - `linkedin_url`: VARCHAR(500), Nullable
  - `github_url`: VARCHAR(500), Nullable
  - `portfolio_url`: VARCHAR(500), Nullable
  - `target_roles`: JSONB, Not Null, Default `[]` (cargos-alvo almejados)
  - `work_modes`: JSONB, Not Null, Default `[]` (ex: `["REMOTE", "HYBRID"]`)
  - `base_resume_raw`: TEXT, Nullable (conteúdo bruto do currículo-base)
  - `created_at`: TIMESTAMP WITH TIME ZONE, Not Null
  - `updated_at`: TIMESTAMP WITH TIME ZONE, Not Null

- **`experiences`**:
  - `id`: UUID (PK)
  - `profile_id`: UUID (FK -> `candidate_profiles.id`, ON DELETE CASCADE)
  - `company`: VARCHAR(255), Not Null
  - `role`: VARCHAR(255), Not Null
  - `location`: VARCHAR(255), Nullable
  - `start_date`: DATE, Not Null
  - `end_date`: DATE, Nullable (null se cargo atual)
  - `is_current`: BOOLEAN, Not Null, Default False
  - `description`: TEXT, Nullable
  - `skills_used`: JSONB, Not Null, Default `[]`
  - `order_index`: INTEGER, Not Null, Default 0

- **`educations`**:
  - `id`: UUID (PK)
  - `profile_id`: UUID (FK -> `candidate_profiles.id`, ON DELETE CASCADE)
  - `institution`: VARCHAR(255), Not Null
  - `degree`: VARCHAR(255), Not Null (ex: "Bacharelado", "Pós-graduação")
  - `field_of_study`: VARCHAR(255), Not Null (ex: "Ciência da Computação")
  - `start_date`: DATE, Nullable
  - `end_date`: DATE, Nullable
  - `order_index`: INTEGER, Not Null, Default 0

- **`skills`**:
  - `id`: UUID (PK)
  - `profile_id`: UUID (FK -> `candidate_profiles.id`, ON DELETE CASCADE)
  - `name`: VARCHAR(100), Not Null
  - `category`: VARCHAR(50), Not Null (ex: "TECHNICAL", "SOFT_SKILL", "LANGUAGE")
  - `proficiency_level`: VARCHAR(50), Nullable (ex: "BEGINNER", "INTERMEDIATE", "ADVANCED", "EXPERT", ou "FLUENT")
  - `evidence`: TEXT, Nullable (projeto ou experiência relacionada)

---

## 3. Contratos de API (FastAPI)

### 3.1 Endpoints

- `GET /api/v1/profile`
  - Retorna o perfil ativo do candidato (como é local-first/single-user no MVP, retorna o perfil cadastrado ou cria default se vazio).
  - Status: `200 OK`.
- `PUT /api/v1/profile`
  - Atualiza atomicamente os dados do perfil, substituindo ou sincronizando entidades filhas (`experiences`, `educations`, `skills`).
  - Status: `200 OK`, `422 Unprocessable Entity` (validação Pydantic).
- `DELETE /api/v1/profile` (Atende RF-12: Privacidade e Exclusão)
  - Limpa todos os dados de perfil e dados correlacionados locais.
  - Status: `204 No Content`.

---

## 4. Frontend & Componentes (React 19 / TypeScript / Tailwind CSS)

### 4.1 Componentes Atômicos Exigidos (`frontend/src/components/ui/`)
1. **`Button`**:
   - Variantes: `primary` (`#6C8CFF`), `secondary` (`#202733` com borda `#303947`), `ghost`, `danger` (`#FF727F`).
   - Estados: `default`, `hover`, `active`, `disabled`, `loading`.
   - Acessibilidade: foco visível via anel de destaque.
2. **`Input` & `Textarea`**:
   - Fundo `#181D25`, borda `#303947`, texto `#F2F5F9`, placeholder `#7E899B`.
   - Estados de erro com borda `#FF727F` e mensagem associada com `aria-describedby`.
3. **`Card`**:
   - Fundo `#181D25`, borda `#303947`, raio `14px` (`rounded-[14px]`).
4. **`Badge`**:
   - Variantes: `neutral`, `brand`, `success` (`#46C99A`), `warning` (`#F2B85B`), `danger` (`#FF727F`).
   - Raio `6px` (`rounded-[6px]`).

### 4.2 Tela de Perfil (`frontend/src/sections/Profile/`)
- Seções bem definidas:
  1. **Dados Básicos & Contato:** Nome, headline, links (LinkedIn, GitHub, Portfólio).
  2. **Objetivos & Modalidades:** Cargos-alvo e preferências (Remoto/Híbrido/Presencial).
  3. **Experiências Profissionais:** Lista cronológica reversa, adição e remoção.
  4. **Formação Acadêmica:** Lista de graduações/cursos.
  5. **Competências & Idiomas:** Tags com categorização visual.
  6. **Currículo-Base Bruto:** Campo de texto/Markdown para importação ou colagem direta com preservação do conteúdo.

---

## 5. Critérios de Aceite (Definition of Done)

1. **[Backend] Validação Estrita:** Nenhum perfil pode ser gravado sem `full_name`. Campos estruturados como listas e datas devem passar por validação estrita no Pydantic.
2. **[Backend] Repositório Isolado:** Toda operação com PostgreSQL é restrita a `backend/app/repositories/profile_repository.py`. Nenhuma consulta SQL em rotas/controllers.
3. **[Backend] Cobertura de Testes (Pytest):** Testes unitários para os schemas e testes de integração cobrindo o fluxo completo dos endpoints da API (`GET`, `PUT`, `DELETE`).
4. **[Frontend] Tipagem Estrita:** TypeScript em modo estrito, zero `any`, interfaces refletindo 1:1 os DTOs do backend.
5. **[Frontend] Cobertura de Testes (Vitest + RTL):** Componentes `Button`, `Input`, `Badge`, `Card` e a tela `ProfileSection` com testes de renderização, interação e acessibilidade.
6. **[Design System]:** Cores, raios e espaçamentos respeitam integralmente os tokens do `DESIGN-SYSTEM.md`.
7. **[Human-in-the-Loop & Governança]:** Exclusão total de dados sob solicitação do usuário em conformidade com o RF-12.

---

## 6. Roteiro Passo a Passo de Ciclos TDD

### **Ciclo 1: Modelos e Repositório (Backend)**
- **1.1 [Test]**: Criar `backend/tests/unit/test_profile_schemas.py` com casos para validação de dados válidos, campos obrigatórios, datas inconsistentes (`end_date` anterior a `start_date`) e sanitização.
- **1.2 [Code]**: Criar schemas Pydantic em `backend/app/models/profile.py`.
- **1.3 [Test]**: Criar `backend/tests/integration/test_profile_repository.py` testando CRUD de perfil com SQLAlchemy em banco isolado.
- **1.4 [Code]**: Criar entidade ORM e repositório em `backend/app/repositories/profile_repository.py` e configuração de banco em `backend/app/core/database.py`.

### **Ciclo 2: Endpoints da API FastAPI (Backend)**
- **2.1 [Test]**: Criar `backend/tests/api/test_profile_api.py` testando `GET /api/v1/profile`, `PUT /api/v1/profile` e `DELETE /api/v1/profile`.
- **2.2 [Code]**: Implementar roteamento FastAPI em `backend/app/api/profile.py` e registrar no `app.main`.

### **Ciclo 3: Componentes Atômicos de UI (Frontend)**
- **3.1 [Test]**: Criar `frontend/src/tests/ui/Button.test.tsx` e `frontend/src/tests/ui/Input.test.tsx`.
- **3.2 [Code]**: Implementar `Button.tsx` e `Input.tsx` com tokens de cores e estados do DS.
- **3.3 [Test]**: Criar `frontend/src/tests/ui/Badge.test.tsx` e `frontend/src/tests/ui/Card.test.tsx`.
- **3.4 [Code]**: Implementar `Badge.tsx` e `Card.tsx`.

### **Ciclo 4: Tela de Perfil e Integração (Frontend)**
- **4.1 [Test]**: Criar `frontend/src/tests/sections/ProfileSection.test.tsx` cobrindo carregamento, preenchimento, validação e envio.
- **4.2 [Code]**: Implementar cliente de API em `frontend/src/services/profileService.ts` e a interface completa em `frontend/src/sections/Profile/ProfileSection.tsx`.
