# Data Model & State: Correção do Erro de Carregamento do Perfil

**Feature**: `002-fix-profile-load-error`  
**Date**: 2026-11-06  

## Frontend UI State Transitions

```mermaid
stateDiagram-v2
    [*] --> Loading: Montagem do componente (useEffect)
    Loading --> Loaded: GET /api/v1/profile (200 OK ou 404 vazio)
    Loading --> OfflineError: Erro de rede (Failed to fetch / 503)
    OfflineError --> Loading: Clique em "Tentar novamente"
    
    Loaded --> Saving: Submissão do formulário (Salvar)
    Saving --> Loaded: Salvo com sucesso (200 OK)
    Saving --> SaveError: Erro ao salvar (rede ou validação)
    SaveError --> Loaded: Usuário edita campos (dados preservados)
```

## Entidades e Tipos de Estado

### 1. `ConnectionState` (Frontend)
Estrutura de estado de feedback no componente `ProfileSection.tsx`:

```typescript
export interface ConnectionError {
  isOffline: boolean;
  message: string;
  detail?: string;
}
```

- **`isOffline`**: `true` quando a requisição falha por queda de rede ou serviço local desligado (`Failed to fetch`).
- **`message`**: Texto principal exibido no banner de alerta ("Serviço local indisponível" vs "Erro ao carregar perfil").
- **`detail`**: Instrução de ação (ex.: "Verifique se a API backend está em execução na porta 8000.").

### 2. `DatabaseConfig` (Backend)
Configuração de conexão no `backend/app/core/database.py`:

- **Primary URL**: `os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/jobmatch_db")`
- **Fallback URL**: `sqlite:///./jobmatch.db`
- **Tabelas criadas**: `candidate_profiles`, `experiences`, `educations`, `skills` (criadas via `Base.metadata.create_all(bind=engine)` caso não existam no SQLite local).

