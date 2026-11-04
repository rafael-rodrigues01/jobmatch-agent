# Changelog - Backend

Todas as mudanças relevantes e versionadas do módulo `backend` serão documentadas neste arquivo.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [0.1.0] - 2026-11-03

### Adicionado (Fase 1 - Fundação / Perfil do Candidato)
- **Modelos e Validações (Pydantic v2):**
  - `CandidateProfileBase`, `CandidateProfileCreate`, `CandidateProfileUpdate` e `CandidateProfileResponse`.
  - Entidades estruturadas: `ExperienceSchema`, `EducationSchema`, `SkillSchema`.
  - Enums de domínio: `WorkMode` (REMOTE, HYBRID, ON_SITE) e `SkillCategory` (TECHNICAL, SOFT_SKILL, LANGUAGE).
  - Validações de integridade em `ExperienceSchema` (datas coerentes e restrição para cargo atual).
- **Persistência Relacional (SQLAlchemy / PostgreSQL):**
  - Tabelas `candidate_profiles`, `experiences`, `educations`, `skills` com suporte a `CASCADE` e timestamps UTC.
  - Conector de banco e gerador de sessão em `app.core.database`.
  - Camada de acesso isolada `CandidateProfileRepository` em `app.repositories.profile_repository` com operações CRUD e conversões DTO.
- **API REST (FastAPI):**
  - Rota `GET /api/v1/profile` para consulta do perfil ativo.
  - Rota `PUT /api/v1/profile` para upsert atômico de dados de perfil, experiências e competências.
  - Rota `DELETE /api/v1/profile` para exclusão e privacidade de dados (RF-12).
  - Ponto de entrada `app.main` com CORS habilitado e endpoint de saúde `/health`.
- **Suíte de Testes Automatizados (Pytest):**
  - Testes unitários de schemas (`tests/unit/test_profile_schemas.py`).
  - Testes de integração de repositório (`tests/integration/test_profile_repository.py`).
  - Testes de integração da API (`tests/api/test_profile_api.py`).
  - 13 testes implementados com 100% de sucesso.
