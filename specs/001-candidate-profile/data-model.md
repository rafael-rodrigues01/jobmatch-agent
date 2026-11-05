# Data Model: Candidate Profile & Base Resume Management (As-Built)

**Feature Branch**: `001-candidate-profile`  
**Date**: 2026-11-04  
**Status**: Implementado no Código

## Diagrama Entidade-Relacionamento Refletido do Código

O modelo reflete diretamente as classes ORM em [`backend/app/models/entities.py`](file:///C:/dev/projects/jobmatch-agent/backend/app/models/entities.py) e os esquemas Pydantic em [`backend/app/models/profile.py`](file:///C:/dev/projects/jobmatch-agent/backend/app/models/profile.py):

```mermaid
erDiagram
    CandidateProfileModel ||--o{ ExperienceModel : "cascade delete-orphan"
    CandidateProfileModel ||--o{ EducationModel : "cascade delete-orphan"
    CandidateProfileModel ||--o{ SkillModel : "cascade delete-orphan"

    CandidateProfileModel {
        string id PK "UUID string(36)"
        string full_name "VARCHAR(255) Not Null"
        string headline "VARCHAR(255) Nullable"
        text summary "TEXT Nullable"
        string email "VARCHAR(255) Nullable"
        string phone "VARCHAR(50) Nullable"
        string location "VARCHAR(255) Nullable"
        string linkedin_url "VARCHAR(500) Nullable"
        string github_url "VARCHAR(500) Nullable"
        string portfolio_url "VARCHAR(500) Nullable"
        json target_roles "JSON Not Null, default []"
        json work_modes "JSON Not Null, default []"
        text base_resume_raw "TEXT Nullable"
        datetime created_at "DateTime Not Null"
        datetime updated_at "DateTime Not Null"
    }

    ExperienceModel {
        string id PK "UUID string(36)"
        string profile_id FK "VARCHAR(36) ondelete CASCADE"
        string company "VARCHAR(255) Not Null"
        string role "VARCHAR(255) Not Null"
        string location "VARCHAR(255) Nullable"
        date start_date "Date Not Null"
        date end_date "Date Nullable"
        boolean is_current "Boolean Not Null, default False"
        text description "TEXT Nullable"
        json skills_used "JSON Not Null, default []"
        integer order_index "Integer Not Null, default 0"
    }

    EducationModel {
        string id PK "UUID string(36)"
        string profile_id FK "VARCHAR(36) ondelete CASCADE"
        string institution "VARCHAR(255) Not Null"
        string degree "VARCHAR(255) Not Null"
        string field_of_study "VARCHAR(255) Not Null"
        date start_date "Date Nullable"
        date end_date "Date Nullable"
        integer order_index "Integer Not Null, default 0"
    }

    SkillModel {
        string id PK "UUID string(36)"
        string profile_id FK "VARCHAR(36) ondelete CASCADE"
        string name "VARCHAR(100) Not Null"
        string category "VARCHAR(50) Not Null (TECHNICAL | SOFT_SKILL | LANGUAGE)"
        string proficiency_level "VARCHAR(50) Nullable"
        text evidence "TEXT Nullable"
    }
```

## Regras de Validação Verificadas em Código

1. **Validação Temporal (`ExperienceSchema.validate_dates`)**:
   - `start_date > end_date` lança `ValueError("end_date must be after start_date")`.
   - `is_current == True` acompanhado de `end_date` lança `ValueError("A current role cannot have an end_date")`.
2. **Obrigatoriedade e Tipagem**:
   - `full_name` obrigatório com `min_length=1`.
   - `WorkMode`: `REMOTE`, `HYBRID`, `ON_SITE`.
   - `SkillCategory`: `TECHNICAL`, `SOFT_SKILL`, `LANGUAGE`.
3. **Persistência Relacional**:
   - Chave estrangeira com `ondelete="CASCADE"` e relacionamento SQLAlchemy com `cascade="all, delete-orphan"`, garantindo que exclusões do perfil excluam todas as entidades associadas.
