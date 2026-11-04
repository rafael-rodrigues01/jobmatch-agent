# Contexto do Sistema e Arquitetura

## Arquitetura de Módulos

```text
jobmatch-agent/
├── backend/
│   ├── app/
│   │   ├── api/             # Rotas e controladores FastAPI
│   │   ├── core/            # Configurações de banco (SQLAlchemy) e segurança
│   │   ├── models/          # Schemas Pydantic (profile.py) e entidades ORM (entities.py)
│   │   ├── repositories/    # Camada isolada de persistência (profile_repository.py)
│   │   ├── services/        # Regras de negócio
│   │   └── adapters/        # Adaptadores externos (futuro: LinkedIn, parsers manuais)
│   ├── tests/               # Testes unitários, de integração e de API (Pytest)
│   └── changelog.md         # Registro de mudanças do backend
├── frontend/
│   ├── src/
│   │   ├── components/ui/   # Componentes atômicos do Design System (Button, Input, Badge, Card)
│   │   ├── sections/        # Visões/Telas (ProfileSection)
│   │   ├── services/        # Clientes HTTP (profileService.ts)
│   │   ├── types/           # Definições estritas TypeScript (profile.ts)
│   │   └── tests/           # Testes unitários e de componentes (Vitest + RTL)
│   ├── changelog.md         # Registro de mudanças do frontend
│   └── vite.config.ts       # Configuração de build e runner de testes
├── specs/                   # Especificações técnicas de cada feature (SDD)
└── docs/                    # PRD.md e DESIGN-SYSTEM.md
```

## Diretrizes de Integração
- **Comunicação Frontend-Backend:** API REST via JSON.
- **Isolamento de Banco:** Toda interação direta com SQLAlchemy/PostgreSQL reside exclusivamente em `backend/app/repositories/`. Controladores dependem apenas das interfaces dos repositórios.
- **Design System:** Padrão escuro fixado via variáveis de tema Tailwind v4 no arquivo `frontend/src/index.css`.
