# Changelog - Frontend

Todas as mudanças relevantes e versionadas do módulo `frontend` serão documentadas neste arquivo.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [0.1.0] - 2026-11-03

### Adicionado (Fase 1 - Fundação / Perfil do Candidato)
- **Infraestrutura e Setup:**
  - Configuração do projeto com React 19, TypeScript estrito (`strict: true`, zero `any`), Vite e Tailwind CSS v4.
  - Setup do Vitest + React Testing Library + Jest-DOM para execução dos testes unitários e de componentes.
  - Tokens semânticos oficiais do Design System escuro injetados no `@theme` (`#101318`, `#181D25`, `#202733`, `#303947`, `#6C8CFF`, etc.).
- **Componentes Atômicos de UI (`components/ui`):**
  - `Button`: Variantes (`primary`, `secondary`, `ghost`, `danger`), foco acessível e indicador `isLoading` com `aria-busy`.
  - `Input`: Rótulo acessível, estilização de foco/borda, estados de erro (`aria-invalid`) e texto auxiliar.
  - `Badge`: Pílulas semânticas de raio 6px (`neutral`, `brand`, `success`, `warning`, `danger`, `info`).
  - `Card`: Superfície elevada com borda e raio 14px, suporte a título, subtítulo e ações.
- **Serviços & Tipagem (`types/` e `services/`):**
  - Tipos TypeScript estritos em `types/profile.ts` espelhando os contratos de dados da API.
  - Cliente de integração HTTP em `services/profileService.ts` (`getProfile`, `saveProfile`, `deleteProfile`).
- **Tela de Perfil (`sections/Profile`):**
  - `ProfileSection`: Edição e visualização completa de dados pessoais, contatos, resumo, lista de experiências, competências validadas e currículo-base em texto/Markdown.
  - Alertas acessíveis de sucesso e falha no salvamento.
- **Suíte de Testes Automatizados (Vitest / RTL):**
  - 12 testes passando cobrindo botões, inputs, cards, badges e a tela `ProfileSection`.
  - Build de produção verificado com sucesso sem erros (`npm run build`).
