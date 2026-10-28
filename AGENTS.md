# JobMatch Agent — Diretrizes, Arquitetura e Regras de Desenvolvimento

## 1. Visão Geral
O **JobMatch Agent** é uma aplicação desktop/local-first focada em produtividade com inteligência artificial para busca, triagem e preparação de candidaturas a vagas de emprego, operando sob o princípio de *human-in-the-loop*.

O sistema automatiza tarefas repetitivas (busca agendada, deduplicação, extração de requisitos, cálculo de aderência e geração de currículo direcionado em Markdown/PDF), mantendo o usuário no controle absoluto de todas as decisões e envios finais.

---

## 2. Stack Tecnológica
- **Backend:** Python 3.11+ / FastAPI
- **Persistência:** PostgreSQL (isolada por camada de acesso/repositório e ORM/migrações)
- **Frontend:** React 19+ / TypeScript (strict mode ativado, zero `any`)
- **Build Tool:** Vite
- **Estilização:** Tailwind CSS v4+ (com tokens do Design System)
- **Ícones:** Lucide React
- **Testes:**
  - Frontend: Vitest + React Testing Library
  - Backend: Pytest
- **Agendador & Automação:** Agendador local com execução configurada (2x ao dia) + execução sob demanda; automação com limites defensivos e fallback para importação manual por URL/texto.

---

## 3. Estrutura de Diretórios
```text
jobmatch-agent/
├── backend/
│   ├── app/
│   │   ├── api/             # Rotas e controladores FastAPI
│   │   ├── core/            # Configurações, segurança e agendador
│   │   ├── models/          # Modelos de dados e schemas (Pydantic / ORM)
│   │   ├── repositories/    # Camada de acesso a dados PostgreSQL
│   │   ├── services/        # Lógica de negócio (match, dedup, IA, resume)
│   │   └── adapters/        # Adaptadores externos (LinkedIn, importador manual)
│   └── tests/               # Testes backend (unitários e integração)
├── frontend/
│   ├── src/
│   │   ├── components/      # Componentes reutilizáveis (Sidebar, Header, Layout)
│   │   │   └── ui/          # Componentes atômicos (Button, Badge, Card, Modal, Input)
│   │   ├── sections/        # Telas/Visões (Dashboard, Jobs, JobDetail, ResumeEditor, Profile, Automation, Settings)
│   │   ├── services/        # Clientes de API e comunicação com backend
│   │   ├── data/            # Dados estáticos, mocks e constantes
│   │   ├── types/           # Definições de tipos TypeScript (estritos)
│   │   └── tests/           # Testes frontend (Vitest + RTL)
├── docs/                    # PRD.md, DESIGN-SYSTEM.md e documentações
├── specs/                   # Especificações técnicas e critérios de aceite (SDD)
└── tests/                   # Testes e2e / cenários ponta a ponta
```

---

## 4. Regras e Restrições para o Agente (IA)

1. **Human-in-the-Loop Obrigatório (Zero Candidatura Automática):**
   - **NUNCA** submeter candidaturas, enviar formulários finais ou disparar mensagens a recrutadores automaticamente.
   - O status `Candidatura enviada pelo usuário` só pode ser aplicado após confirmação explícita do usuário.
2. **Zero Alucinação de Dados Profissionais:**
   - **NUNCA** inventar experiências, competências, números, métricas ou certificações.
   - Tratar o perfil do candidato como única fonte da verdade. O que não constar no perfil deve ser marcado como lacuna ("Não comprovado no perfil") ou omitido.
3. **Respeito a Barreiras e Controles Anti-Bot:**
   - **NUNCA** tentar contornar CAPTCHAs, MFA, paywalls ou mecanismos de proteção.
   - Diante de desafios de acesso, sessão expirada ou páginas inesperadas, **pausar a automação imediatamente** e solicitar intervenção humana.
4. **Privacidade, Segurança e Persistência:**
   - Armazenar dados no PostgreSQL mantendo acesso isolado pela camada de repositórios.
   - Segredos, tokens, strings de conexão e chaves de API nunca devem ser salvos em texto puro no repositório nem expostos em logs (usar variáveis de ambiente/`.env`).
   - Sanitizar logs estruturados. Minimizar dados pessoais enviados aos provedores de IA.
5. **Spec-Driven Development (SDD):**
   - Toda implementação deve ser precedida por especificação técnica em `specs/`. Os critérios de aceite do PRD e das specs são a definição estrita de conclusão ("Definition of Done").
6. **TDD / Testes Obrigatórios:**
   - Nenhum endpoint, adaptador, serviço ou componente de UI deve ser criado sem testes correspondentes (Pytest para Python, Vitest/RTL para React).
7. **TypeScript & Python Estritos:**
   - Zero `any` e sem type assertions forçadas no frontend.
   - Tipagem completa com type hints e Pydantic no backend.
8. **Sem Pacotes Extras sem Permissão:**
   - Não executar instalações de novas bibliotecas sem justificar e obter autorização prévia.
9. **Desacoplamento e Resiliência:**
   - A lógica de negócio não pode depender diretamente do DOM de plataformas externas nem de provedores específicos de LLM.
   - Falhas na captura ou análise de uma vaga não devem interromper o processamento das demais. Fornecer sempre importação manual por URL/texto como fallback.

---

## 5. Diretrizes de Design & Paleta (Design System Tokens)

### 5.1 Paleta de Cores (Tema Escuro / Profissional Produtivo)
- **Fundo da aplicação (`color.bg.canvas`):** `#101318`
- **Cards e superfícies (`color.bg.surface`):** `#181D25`
- **Superfícies elevadas / Modais / Menus (`color.bg.elevated`):** `#202733`
- **Bordas e divisores (`color.border.default`):** `#303947`
- **Texto Principal (`color.text.primary`):** `#F2F5F9`
- **Texto Secundário (`color.text.secondary`):** `#A7B1C2`
- **Texto Atenuado / Metadados (`color.text.muted`):** `#7E899B`
- **Ação Primária / Brand (`color.brand.primary`):** `#6C8CFF`
- **Acentos de IA (`color.brand.secondary`):** `#9B8AFB`

### 5.2 Cores de Status Semântico
- **Sucesso / Atendido (`color.status.success`):** `#46C99A`
- **Atenção / Revisão (`color.status.warning`):** `#F2B85B`
- **Erro / Bloqueio / Perigo (`color.status.danger`):** `#FF727F`
- **Informação / Em andamento (`color.status.info`):** `#63B8F5`

### 5.3 Tipografia, Espaçamento e Componentes
- **Tipografia:** Fonte principal **Inter** (fallbacks: `system-ui`, `Segoe UI`, `sans-serif`).
- **Espaçamento:** Múltiplos de 4px (`space.1`: 4px, `space.2`: 8px, `space.3`: 12px, `space.4`: 16px, `space.6`: 24px, `space.8`: 32px).
- **Raios de Borda:** `radius.sm`: 6px (badges), `radius.md`: 10px (inputs/botões), `radius.lg`: 14px (cards), `radius.xl`: 18px (modais).
- **Indicador de Aderência:** Explicável, nunca pontuação isolada (80–100: *Alta correspondência*, 60–79: *Correspondência moderada*, 0–59: *Baixa correspondência*).
- **Badges de Status da Vaga:** `Nova`, `Analisada`, `Revisar`, `Currículo preparado`, `Em preparação`, `Enviada pelo usuário`, `Ignorada`, `Arquivada`.
- **Acessibilidade:** Conformidade WCAG AA, navegação completa por teclado, contraste alto, foco visível e status comunicados por texto além de cor.
