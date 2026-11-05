# Contexto Ativo

## Foco Atual
- Preparação para a **Fase 2 do PRD: Vagas (Coleta, Normalização e Deduplicação)** após conclusão e convergência de 100% da Fase 1 (Perfil do Candidato).

## Estado do Repositório
- **Módulo 001 (Candidate Profile)**: Totalmente convergido com a especificação, plano técnico e tarefas em `specs/001-candidate-profile/`.
- **Tríade de Qualidade Pré-CI/CD**:
  - Pytest: 13/13 testes passando.
  - Vitest: 12/12 testes passando.
  - TypeScript/Build: 0 erros, compilação de produção limpa.

## Próximos Passos Imediatos
1. Iniciar a nova especificação via comando:
   ```text
   /speckit-specify Descreva a funcionalidade de ingestão e normalização de vagas
   ```
2. Mapear os requisitos da Fase 2 (RF-04: Captura e Importação de Vagas, RF-05: Deduplicação e Identificação de Vagas, RF-10: Gestão do Funil e Status).
3. Definir as entidades de banco de dados (`Job`, `JobSource`, `ApplicationActivity`) e endpoints da API de vagas.
