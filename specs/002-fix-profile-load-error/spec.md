# Feature Specification: Correção do Erro de Carregamento do Perfil no Frontend

**Feature Branch**: `002-fix-profile-load-error`

**Created**: 2026-11-06

**Status**: Ready for Planning

**Input**: User description: "Correção de Bug: quando tô abrindo meu frontend tá aparecendo uma mensagem em vermelho dizendo que: Não foi possível carregar os dados do perfil."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Diagnóstico Claro e Ação Diante da Indisponibilidade do Backend/Banco (Priority: P1)

Como um usuário abrindo o frontend do JobMatch Agent,  
Quero receber uma mensagem explicativa, contextualizada e amigável quando o serviço de backend ou banco de dados local não estiver acessível, acompanhada de instruções para diagnóstico e botão de nova tentativa ("Tentar novamente"),  
Para que eu saiba exatamente o que está acontecendo sem ficar bloqueado diante de uma mensagem genérica e consiga restabelecer a conexão.

**Why this priority**: É a causa direta da mensagem de erro relatada pelo usuário na inicialização. Comunica honestamente o estado do sistema (conforme o Design System) e oferece ação de recuperação.

**Independent Test**: Pode ser testado abrindo o frontend com o backend parado ou inacessível: a aplicação deve exibir banner explicativo informando indisponibilidade do serviço e botão "Tentar novamente" que dispara nova tentativa de carregamento ao ser clicado.

**Acceptance Scenarios**:

1. **Given** o usuário abre a aplicação e a conexão com a API falha (ex.: serviço offline ou erro de rede), **When** a tentativa de carregar o perfil falha, **Then** o sistema exibe alerta explicativo informando que o serviço local está indisponível, sugerindo verificar se a API e o banco estão em execução, e apresenta botão de "Tentar novamente".
2. **Given** o alerta de serviço indisponível em exibição, **When** o usuário inicia o serviço de backend e clica em "Tentar novamente", **Then** a aplicação recarrega os dados com sucesso, remove o alerta de erro e exibe os dados do perfil ou formulário pronto para uso.

---

### User Story 2 - Resiliência e Fallback Local de Persistência (Priority: P2)

Como um usuário executando a aplicação desktop/local-first,  
Quero que o backend consiga inicializar em modo local autônomo (com fallback para banco local SQLite se o PostgreSQL não estiver ativo ou configurado),  
Para que eu consiga utilizar a aplicação de busca e currículo imediatamente sem exigir obrigatoriamente um servidor PostgreSQL pré-configurado ativo na máquina.

**Why this priority**: Reduz atrito no ambiente local de desenvolvimento/desktop, garantindo que o backend inicie e responda à rota `/api/v1/profile` mesmo quando o serviço do PostgreSQL estiver parado.

**Independent Test**: Iniciar o backend sem PostgreSQL rodando na porta 5432; o backend deve utilizar o fallback local seguro (ex.: SQLite local) sem levantar erro de conexão recusada e responder com status 200 na rota de perfil.

**Acceptance Scenarios**:

1. **Given** o backend configurado sem conexão ativa com PostgreSQL, **When** a API inicia e tenta conectar, **Then** ela inicializa com fallback local transparente e seguro, registrando no log o modo ativo e permitindo que o endpoint `/api/v1/profile` funcione normalmente.
2. **Given** o backend respondendo normalmente, **When** o frontend requisita os dados, **Then** nenhum alerta vermelho de erro é exibido e a tela carrega o perfil (ou estado inicial pronto para preenchimento).

---

### Edge Cases

- **Timeout de Conexão**: Se a API demorar mais de 5 segundos para responder, a requisição deve ser cancelada com feedback de "Tempo de resposta esgotado" e permitir nova tentativa sem travar a interface.
- **Perfil Inexistente (404)**: Quando o perfil ainda não foi cadastrado, o sistema trata como formulário novo/vazio sem disparar alerta vermelho de erro.
- **Interrupção de Rede durante Salvamento**: Caso a conexão caia durante a gravação, os dados locais digitados no formulário devem ser preservados na tela, alertando sobre a falha sem descartar o texto digitado.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O frontend DEVE distinguir falha de rede/serviço offline de erro de validação ou perfil não encontrado (404).
- **FR-002**: O frontend DEVE exibir feedback acessível e contextualizado (banner com papel `alert` e cores semânticas do Design System `#FF727F`/`#F2B85B`) quando o backend estiver inalcançável.
- **FR-003**: O frontend DEVE disponibilizar uma ação interativa ("Tentar novamente" / "Reconectar") para reexecutar a busca dos dados do perfil sob demanda sem necessitar recarregar toda a página no navegador.
- **FR-004**: O frontend DEVE manter os dados preenchidos pelo usuário no estado do formulário se uma falha de conexão ocorrer durante a sessão, prevenindo perda de digitação.
- **FR-005**: O backend DEVE registrar erro sanitizado de conexão de forma estruturada nos logs quando não for possível alcançar a persistência principal.
- **FR-006**: O backend DEVE possuir configuração defensiva de fallback para persistência local (SQLite em arquivo local) caso a URL padrão do PostgreSQL não esteja acessível no ambiente local-first.

### Key Entities

- **ProfileState**: Estado de carregamento do perfil no frontend (`idle`, `loading`, `success`, `error`, `offline`).
- **ConnectionStatus**: Diagnóstico da conexão do cliente com o serviço local da API.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: O alerta vermelho genérico "Não foi possível carregar os dados do perfil." é substituído por mensagem contextualizada com orientação clara e botão de reiteração em 100% dos cenários de indisponibilidade de backend.
- **SC-002**: O tempo para recuperar a interface após restabelecimento do serviço é de menos de 2 segundos após clique em "Tentar novamente", sem recarregar o navegador.
- **SC-003**: Zero perda de dados digitados pelo usuário em caso de queda transitória de conexão.
- **SC-004**: 100% dos testes unitários e de componentes do frontend e backend continuam passando com validação em verde.

## Assumptions

- O frontend está rodando localmente (Vite na porta padrão 5173) e busca a API em `http://localhost:8000/api/v1`.
- A mensagem de erro em vermelho ocorre quando o frontend tenta realizar a chamada `GET /api/v1/profile` e a API não está respondendo (ou a API respondeu erro 500 devido à falta de conexão com o banco de dados).
- O usuário deve ser capaz de utilizar o JobMatch Agent mesmo em computadores sem PostgreSQL instalado, por meio de fallback de armazenamento local.

