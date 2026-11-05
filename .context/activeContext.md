# Contexto Ativo

## Foco Atual
- **Sessão encerrada**. Base consolidada e pronta para a **Fase 2 do PRD: Vagas (Coleta, Normalização e Deduplicação)** na próxima sessão.

## Estado do Repositório (Branch: main)
- **Módulo 001 (Candidate Profile)**: 100% implementado, testado e formalizado com artefatos Spec-Kit em `specs/001-candidate-profile/`.
- **Pipeline CI/CD (.github/workflows/ci.yml)**:
  - Job `validate-frontend`: Node 20, cache npm, `npm ci`, lint, Vitest (12 testes OK), build de produção Vite.
  - Job `validate-backend`: Python 3.11, cache pip, `requirements.txt`, Pytest (13 testes OK) com `PYTHONPATH: .`.
- **Tríade de Qualidade Pré-CI/CD**:
  - Backend Pytest: 13/13 testes passando.
  - Frontend Vitest: 12/12 testes passando.
  - TypeScript/Build: 0 erros, compilação estrita e limpa.
- **Histórico de Commits Recentes**:
  - `08dbd0b`: Formalização dos artefatos Spec-Kit e documentação de contexto.
  - `c3699a8`: Ajuste de diretório de trabalho e cache do frontend no CI.
  - `d95d924`: Criação de `backend/requirements.txt` e configuração do pipeline Python no CI.

## Próximos Passos Imediatos (Próxima Sessão)
1. Iniciar a especificação da Fase 2 via Spec-Kit:
   ```text
   /speckit-specify Descreva a funcionalidade de ingestão manual e normalização de vagas
   ```
2. Mapear os requisitos de negócio e aceitação da Fase 2:
   - **RF-04**: Captura e Importação de Vagas (URL e texto bruto).
   - **RF-05**: Deduplicação e Identificação de Vagas (hash canônico de URL e identificador de publicação).
   - **RF-10**: Gestão de Funil e Status (`Nova`, `Analisada`, `Revisar`, etc.).
3. Desenvolver o modelo de dados de vagas (`Job`, `JobSource`, `ApplicationActivity`) e endpoints da API FastAPI seguindo TDD.
