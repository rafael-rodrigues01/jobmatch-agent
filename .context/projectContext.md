# Contexto do Projeto

## Visão Geral
O **JobMatch Agent** é uma aplicação desktop/local-first focada em produtividade com inteligência artificial para busca, triagem e preparação de candidaturas a vagas de emprego, operando sob o princípio de **human-in-the-loop**.

## Pilares Inegociáveis
1. **Human-in-the-Loop Obrigatório:** Nenhuma candidatura é enviada de forma autônoma.
2. **Zero Alucinação de Dados Profissionais:** O perfil do candidato é a única fonte da verdade. O que não constar nele nunca pode ser inventado.
3. **Respeito a Barreiras Anti-bot:** Em desafios/CAPTCHAs, pausar imediatamente e solicitar intervenção humana.
4. **Privacidade e Persistência Local:** PostgreSQL com camada de repositório isolada; dados locais sob controle total do usuário (RF-12).
5. **Spec-Driven Development (SDD) & TDD:** Toda feature nasce de especificação em `specs/` e é construída pelo ciclo estrito Vermelho -> Verde -> Refatoração.

## Tecnologias Principais
- **Backend:** Python 3.11+, FastAPI, SQLAlchemy, Alembic, PostgreSQL, Pydantic v2, Pytest.
- **Frontend:** React 19, TypeScript estrito, Vite, Tailwind CSS v4, Lucide React, Vitest, React Testing Library.
