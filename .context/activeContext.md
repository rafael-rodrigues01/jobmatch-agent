# Contexto Ativo

## Foco Atual
- **Sessão Concluída**: Correção do erro de carregamento do perfil no frontend (`002-fix-profile-load-error`) e estabilização de resiliência local-first.
- Pronto para a **Fase de Vagas (Coleta, Ingestão Manual, Normalização e Deduplicação)** na próxima sessão.

## Estado do Repositório (Branch: main)
- **Módulo 001 (Candidate Profile)**: 100% implementado e testado.
- **Módulo 002 (Fix Profile Load Error & Local Resiliency)**: 100% implementado via Spec-Kit (`specs/002-fix-profile-load-error/`):
  - Frontend: captura de erro de rede com classe customizada `ApiConnectionError`, banner informativo contextualizado do Design System (`#F2B85B` warning) e botão interativo de **"Tentar novamente"** sem perda de dados do formulário.
  - Backend: fallback automático defensivo para SQLite local (`sqlite:///./jobmatch.db`) no startup caso o PostgreSQL local (porta 5432) não esteja em execução, eliminando falhas de conexão recusada no desktop.
  - Criação do `backend/pytest.ini` para resolução automática de `pythonpath = .` ao rodar testes.
- **Tríade de Qualidade Pré-CI/CD**:
  - Backend Pytest: 14/14 testes passando em verde (incluindo teste de integração do fallback de banco).
  - Frontend Vitest: 15/15 testes passando em verde (incluindo testes de conexão e retry).
  - TypeScript/Build: 0 erros, compilação estrita e limpa (`tsc -b && vite build`).
- **Histórico de Commits Recentes**:
  - `f6e2767`: `fix: handle offline backend gracefully and add sqlite fallback`.
  - `5f2f078`: `remove: remover arquivo antigo de specs`.
  - `3da8523`: `docs: finalize context documentation and wrap up development session`.

## Próximos Passos Imediatos (Próxima Sessão)
1. Iniciar a especificação de ingestão e deduplicação de vagas via Spec-Kit:
   ```text
   /speckit-specify "Fase de Vagas: Cadastro manual e importação por URL/texto com normalização e deduplicação"
   ```
2. Mapear requisitos de negócio do PRD:
   - **RF-04**: Captura e Importação de Vagas (URL e texto bruto com campos estruturados).
   - **RF-05**: Deduplicação e Identificação de Vagas (hash canônico de URL e identificador de publicação).
   - **RF-10**: Gestão de Funil e Status (`Nova`, `Analisada`, `Revisar`, `Currículo preparado`, `Em preparação`, `Enviada pelo usuário`, `Ignorada`, `Arquivada`).
3. Modelagem de dados de vagas (`JobModel`, `JobAnalysisModel`, etc.) e rotas RESTful FastAPI no backend, seguidas pela tela de listagem e detalhe no frontend com TDD.
