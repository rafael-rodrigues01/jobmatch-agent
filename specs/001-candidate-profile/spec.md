# Feature Specification: Candidate Profile & Base Resume Management

**Feature Branch**: `001-candidate-profile`

**Created**: 2026-11-04

**Status**: Implemented & Validated

**Input**: User description: "inclua os arquivos da minha antiga pasta ./specs para gerar a especificação base." (Consolidação e alinhamento com a implementação existente em `backend/app/` e `frontend/src/`).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Cadastro e Manutenção do Perfil Profissional (Priority: P1)

Como um candidato em busca de vagas de emprego,  
Quero cadastrar e gerenciar meus dados básicos, informações de contato, links profissionais e objetivos de carreira,  
Para que o assistente inteligente tenha os dados cadastrais necessários para centralizar minha identidade profissional.

**Why this priority**: É a espinha dorsal de qualquer processo seletivo e o ponto de partida de dados obrigatórios para contato e correspondência de oportunidades.

**Independent Test**: Testado ponta a ponta via `backend/tests/api/test_profile_api.py` e `frontend/src/tests/sections/ProfileSection.test.tsx`, garantindo que inserção, atualização e recarga preservem todos os dados.

**Acceptance Scenarios**:

1. **Given** um candidato acessando a tela de perfil, **When** preenche seu nome completo, headline, contato (e-mail/telefone), links profissionais (LinkedIn, GitHub, portfólio) e cargos-alvo e clica em salvar, **Then** a API persiste os dados e a interface exibe badge/notificação de sucesso sem recarregar a página.
2. **Given** um perfil já existente, **When** o candidato altera seu cargo-alvo ou links e confirma, **Then** as alterações são gravadas atomicamente sem perda de dados prévios.
3. **Given** uma tentativa de salvar o perfil sem preenchimento do nome completo, **When** o formulário é submetido, **Then** a validação estrita (Pydantic no backend / HTML5 + estado no frontend) rejeita com erro `422 Unprocessable Entity` ou indicação visual de erro.

---

### User Story 2 - Gestão Estruturada de Histórico e Competências (Priority: P1)

Como um candidato,  
Quero detalhar minhas experiências profissionais anteriores, formações acadêmicas e competências/idiomas categorizados,  
Para que o sistema possua a única fonte da verdade de evidências profissionais, impedindo qualquer alucinação de dados em etapas futuras de triagem e currículo.

**Why this priority**: A comparação de requisitos com descrições de vagas depende fundamentalmente da rastreabilidade e granularidade das experiências, habilidades e formações cadastradas.

**Independent Test**: Testado por testes unitários (`backend/tests/unit/test_profile_schemas.py`) e de repositório (`backend/tests/integration/test_profile_repository.py`), cobrindo relacionamentos com exclusão órfã (`cascade="all, delete-orphan"`).

**Acceptance Scenarios**:

1. **Given** o formulário de perfil, **When** o candidato adiciona uma experiência profissional com empresa, cargo, período (início e término ou indicativo de cargo atual), descrição e competências utilizadas, **Then** o registro é salvo com relacionamento 1:N ordenado por `order_index`.
2. **Given** a adição de competências ou idiomas, **When** o candidato especifica categoria (`TECHNICAL`, `SOFT_SKILL`, `LANGUAGE`) e proficiência, **Then** os dados são tipados estritamente e persistidos.
3. **Given** uma experiência onde a data final é anterior à data de início ou onde cargo atual possui `end_date`, **When** é submetido, **Then** o validador Pydantic (`validate_dates`) rejeita a operação com mensagem explicativa.

---

### User Story 3 - Preservação do Currículo-Base Bruto (Priority: P2)

Como um candidato,  
Quero armazenar a versão textual completa do meu currículo-base (em texto simples ou Markdown),  
Para que o conteúdo original de redação seja preservado na íntegra sem qualquer mutação automática indesejada.

**Why this priority**: Oferece segurança ao usuário de manter seu currículo original intacto enquanto permite extrair texto e insumos para as próximas fases.

**Independent Test**: Validado no repositório e na API persistindo strings Markdown contendo caracteres especiais, quebras de linha e símbolos, assegurando correspondência idêntica.

**Acceptance Scenarios**:

1. **Given** o candidato possuindo um currículo pré-existente em Markdown/texto, **When** cola o texto na área de currículo-base e salva, **Then** o sistema armazena o conteúdo no campo `base_resume_raw` sem modificações sintáticas.
2. **Given** o texto de currículo-base armazenado, **When** a API `GET /api/v1/profile` é consultada, **Then** o conteúdo é retornado integralmente idêntico ao gravado.

---

### User Story 4 - Privacidade, Controle e Exclusão Total de Dados Locais (Priority: P3)

Como um candidato preocupado com privacidade e soberania de dados,  
Quero poder excluir todos os dados do meu perfil e itens associados com um único comando de limpeza,  
Para ter garantia total de descarte e conformidade com o RF-12 e as regras de governança do `AGENTS.md`.

**Why this priority**: Garante soberania e direito ao esquecimento e descarte limpo de informações locais sensíveis.

**Independent Test**: Testado no endpoint `DELETE /api/v1/profile` (`backend/tests/api/test_profile_api.py`) verificando status HTTP 204 e garantindo que consultas subsequentes retornem 404 Not Found.

**Acceptance Scenarios**:

1. **Given** um perfil preenchido com experiências, formação e competências, **When** o usuário aciona a exclusão definitiva, **Then** o repositório executa a limpeza em cascata no banco de dados e retorna `204 No Content`.
2. **Given** a exclusão concluída, **When** `GET /api/v1/profile` é executado, **Then** a resposta é `404 Not Found`.

---

### Edge Cases

- Se o usuário marcar `is_current: true` e enviar `end_date`, o validador `@model_validator` rejeita o payload informando que um cargo atual não pode ter data de término.
- Se `end_date < start_date`, o validador rejeita com erro explícito de intervalo temporal.
- Falhas de banco durante o upsert realizam rollback automático da transação do SQLAlchemy, mantendo o estado anterior consistente.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema DEVE fornecer os endpoints `GET /api/v1/profile`, `PUT /api/v1/profile` e `DELETE /api/v1/profile`.
- **FR-002**: O sistema DEVE exigir o preenchimento de `full_name` como campo estritamente obrigatório (não nulo e não vazio).
- **FR-003**: O sistema DEVE armazenar campos de contato (`email`, `phone`, `location`, `linkedin_url`, `github_url`, `portfolio_url`) e arrays JSON (`target_roles`, `work_modes`).
- **FR-004**: O sistema DEVE gerenciar a relação 1:N com a entidade `ExperienceModel` (`company`, `role`, `location`, `start_date`, `end_date`, `is_current`, `description`, `skills_used`, `order_index`).
- **FR-005**: O sistema DEVE gerenciar a relação 1:N com a entidade `EducationModel` (`institution`, `degree`, `field_of_study`, `start_date`, `end_date`, `order_index`).
- **FR-006**: O sistema DEVE gerenciar a relação 1:N com a entidade `SkillModel` (`name`, `category`, `proficiency_level`, `evidence`).
- **FR-007**: O sistema DEVE validar consistência cronológica em experiências e cursos, rejeitando registros com datas finais anteriores às datas iniciais.
- **FR-008**: O sistema DEVE armazenar e retornar `base_resume_raw` como texto puro sem qualquer mutação automática.
- **FR-009**: O sistema DEVE executar exclusão em cascata (`cascade="all, delete-orphan"` e `ondelete="CASCADE"`) no endpoint `DELETE /api/v1/profile`.
- **FR-010**: A interface React DEVE utilizar os componentes atômicos do Design System (`Button`, `Input`, `Badge`, `Card`) com conformidade WCAG AA e tipagem estrita sem `any`.

### Key Entities

- **CandidateProfileModel / CandidateProfile**: Representa a identidade central do candidato e agrega experiências, formações e habilidades.
- **ExperienceModel / Experience**: Histórico profissional cronológico reversível com vínculo à chave estrangeira `profile_id`.
- **EducationModel / Education**: Histórico educacional e acadêmico vinculado a `profile_id`.
- **SkillModel / Skill**: Competências técnicas, interpessoais e idiomas categorizados vinculados a `profile_id`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% dos testes unitários e de integração do backend executados com sucesso via Pytest (`13 passed`).
- **SC-002**: 100% dos testes de frontend executados com sucesso via Vitest (`12 passed`).
- **SC-003**: 100% de compilação limpa em TypeScript com `tsc -b` (`zero any`, zero warnings bloqueantes) e bundle gerado pelo Vite.
- **SC-004**: Todas as consultas de persistência PostgreSQL são estritamente isoladas em `CandidateProfileRepository`, sem SQL solto em controladores.
- **SC-005**: Conformidade visual e semântica com o Design System (`#101318` canvas, `#181D25` surface, `#202733` elevated, `#303947` border, `#6C8CFF` brand).

## Assumptions

- A aplicação é local-first/desktop, operando com um perfil ativo único por instância de banco de dados neste MVP.
- O banco de dados configurado em `.env` é PostgreSQL (ou SQLite em memória para a suíte de testes automatizados do Pytest).
- O módulo implementado atende plenamente aos requisitos RF-01, RF-02 e RF-12 do PRD.md.
