# JobMatch Agent --- Design System

**Versão:** 1.0\
**Status:** Proposta inicial para o MVP\
**Produto:** Aplicação desktop/local-first para busca e preparação de
candidaturas

## 1. Direção visual

O JobMatch Agent deve parecer uma ferramenta profissional de
produtividade, confiável e objetiva --- não um chatbot genérico nem um
painel corporativo excessivamente denso.

### Princípios

1.  **Clareza antes de decoração:** a vaga, a aderência e a próxima ação
    devem ser fáceis de identificar.
2.  **Confiança explicável:** pontuações sempre acompanhadas de
    evidências e lacunas.
3.  **Ação humana evidente:** revisão e confirmação são parte central do
    fluxo.
4.  **Densidade controlada:** listas de vagas podem ser compactas;
    análise e currículo precisam de espaço.
5.  **Estados honestos:** distinguir carregamento, sucesso parcial,
    erro, pausa e necessidade de intervenção.
6.  **Privacidade visível:** deixar claro quando dados são enviados a um
    serviço externo.

## 2. Identidade e personalidade

-   **Personalidade:** inteligente, pragmática, confiável, discreta.
-   **Tom de voz:** direto, acolhedor e sem promessas exageradas.
-   **Mensagens:** explicar o que aconteceu, por que aconteceu e o que o
    usuário pode fazer.
-   **Evitar:** "vaga perfeita", "garantia de aprovação ATS",
    "candidatura enviada" quando o usuário ainda não confirmou.

Exemplo de mensagem adequada: "Encontramos 8 vagas novas. 3 têm boa
correspondência com seu perfil; revise os requisitos que ainda não estão
comprovados."

## 3. Cores

Paleta inicial em tema escuro, com contraste e estados semânticos
claros.

  -------------------------------------------------------------------------
  Token                     Valor                   Uso
  ------------------------- ----------------------- -----------------------
  `color.bg.canvas`         `#101318`               Fundo geral

  `color.bg.surface`        `#181D25`               Cards e painéis

  `color.bg.elevated`       `#202733`               Menus, popovers e
                                                    superfícies elevadas

  `color.border.default`    `#303947`               Bordas e separadores

  `color.text.primary`      `#F2F5F9`               Texto principal

  `color.text.secondary`    `#A7B1C2`               Texto secundário

  `color.text.muted`        `#7E899B`               Metadados e dicas

  `color.brand.primary`     `#6C8CFF`               Ações principais e foco

  `color.brand.secondary`   `#9B8AFB`               Acentos e elementos de
                                                    IA

  `color.status.success`    `#46C99A`               Sucesso e requisitos
                                                    atendidos

  `color.status.warning`    `#F2B85B`               Atenção e revisão
                                                    necessária

  `color.status.danger`     `#FF727F`               Erros e ações
                                                    bloqueadas

  `color.status.info`       `#63B8F5`               Informação e atividade
                                                    em andamento
  -------------------------------------------------------------------------

### Regras de cor

-   Não usar a cor como único indicador de estado; sempre combinar com
    texto ou ícone.
-   Usar o azul principal para a ação primária, sem espalhar acentos em
    todos os elementos.
-   Verde significa condição positiva, não "garantia de contratação".
-   Amarelo indica revisão ou informação incompleta.
-   Vermelho é reservado para erros, riscos ou ações bloqueadas.
-   Validar contraste WCAG AA, especialmente para texto pequeno.

## 4. Tipografia

**Fonte preferencial:** Inter.\
**Fallbacks:** system-ui, Segoe UI, sans-serif.

  -------------------------------------------------------------------------
  Estilo                       Tamanho                 Peso Uso
  --------------- -------------------- -------------------- ---------------
  Display                32 px / 2 rem                  700 Título
                                                            principal do
                                                            dashboard,
                                                            quando
                                                            necessário

  H1                  28 px / 1.75 rem                  700 Título de
                                                            página

  H2                 22 px / 1.375 rem                  650 Seções
                                                            principais

  H3                 18 px / 1.125 rem                  600 Títulos de
                                                            cards e painéis

  Body               14 px / 0.875 rem                  400 Texto principal

  Body strong        14 px / 0.875 rem                  600 Labels e
                                                            ênfases

  Small               12 px / 0.75 rem                  400 Metadados e
                                                            ajuda

  Metric                     24--32 px                  700 Contagens e
                                                            métricas
  -------------------------------------------------------------------------

-   Usar altura de linha entre 1.4 e 1.6 para textos longos.
-   Evitar blocos longos em caixa alta.
-   Descrições de vagas devem priorizar legibilidade em vez de
    compactação extrema.

## 5. Espaçamento, raio e elevação

Base de espaçamento: múltiplos de 4 px.

  Token          Valor
  ------------ -------
  `space.1`       4 px
  `space.2`       8 px
  `space.3`      12 px
  `space.4`      16 px
  `space.5`      20 px
  `space.6`      24 px
  `space.8`      32 px
  `space.10`     40 px
  `space.12`     48 px

  Token                Valor Uso
  ------------------ ------- ---------------------------------
  `radius.sm`           6 px Badges e controles compactos
  `radius.md`          10 px Inputs e botões
  `radius.lg`          14 px Cards e painéis
  `radius.xl`          18 px Modais e áreas de destaque
  `shadow.card`        Sutil Separar superfícies sem exagero
  `shadow.overlay`     Média Menus, popovers e modais

Evitar sombras coloridas intensas e bordas decorativas em excesso.

## 6. Layout e navegação

### Estrutura desktop

-   **Sidebar:** largura aproximada de 232 px, com navegação principal.
-   **Área principal:** largura flexível; conteúdo máximo sugerido de
    1440 px.
-   **Header:** título/contexto da página, busca global opcional e
    estado do agente.
-   **Conteúdo:** grids responsivos e painéis com alinhamento
    consistente.
-   **Notificações:** feedback próximo da ação; alertas persistentes
    somente para falhas ou intervenções necessárias.

### Navegação principal

1.  Visão geral
2.  Vagas
3.  Perfil e currículo
4.  Buscas e automação
5.  Histórico
6.  Configurações

O estado de pausa do agente deve ser visível, mas não competir com o
conteúdo principal.

### Responsividade

-   Desktop é o alvo primário do MVP.
-   Em larguras menores, sidebar recolhe para navegação compacta.
-   Tabelas devem se transformar em cards ou permitir rolagem horizontal
    sem esconder ações essenciais.
-   A tela de currículo deve manter o editor utilizável; evitar colunas
    muito estreitas.

## 7. Componentes

### Botões

Variantes: - **Primary:** ação principal da tela, por exemplo "Gerar
currículo". - **Secondary:** ação alternativa, por exemplo "Executar
busca". - **Tertiary/Ghost:** ações menos frequentes. - **Danger:**
exclusão ou interrupção destrutiva, com confirmação quando apropriado.

Estados: default, hover, focus-visible, active, disabled, loading.

Regras: - Usar rótulos verbais específicos. - Não usar "OK" para ações
com consequências. - Botões de envio final de candidatura não fazem
parte do fluxo automatizado do produto.

### Inputs e filtros

-   Labels persistentes; placeholder não substitui label.
-   Indicar campos obrigatórios e erros junto ao campo.
-   Busca com debounce e botão para limpar.
-   Filtros ativos devem aparecer como chips removíveis.
-   Teclado e leitores de tela devem conseguir identificar cada
    controle.

### Cards de vaga

Cada card deve mostrar, nesta ordem: 1. Cargo e empresa. 2.
Localidade/modalidade e data da captura ou publicação, se disponível. 3.
Indicador de aderência acompanhado de rótulo. 4. Até três competências
ou requisitos relevantes. 5. Status e ação principal.

Não mostrar a pontuação isolada como se fosse uma probabilidade de
contratação. Informações ausentes devem ser omitidas ou explicitamente
marcadas.

### Indicador de aderência

Rótulos sugeridos: - 80--100: "Alta correspondência" - 60--79:
"Correspondência moderada" - 0--59: "Baixa correspondência"

Essas faixas são heurísticas configuráveis e devem ser validadas com uso
real. Exibir "Análise incompleta" quando faltarem dados essenciais.
Mostrar detalhes que contribuíram para a avaliação.

### Badges de status

-   Nova
-   Analisada
-   Revisar
-   Currículo preparado
-   Em preparação
-   Enviada pelo usuário
-   Ignorada
-   Arquivada

O badge "Enviada pelo usuário" nunca pode ser aplicado automaticamente
sem confirmação.

### Painéis de evidência

Separar em: - **Corresponde ao perfil** - **Não comprovado no perfil** -
**Requisitos da vaga** - **Pontos para confirmar**

Cada item deve indicar se é dado do perfil, trecho da vaga ou inferência
do modelo. Inferências devem ser claramente rotuladas.

### Tabelas e listas

-   Cabeçalho persistente quando a lista for longa.
-   Ordenação com indicação visual e acessível.
-   Estados vazios que ensinam a próxima ação.
-   Não esconder ações importantes em hover-only.
-   Permitir ordenação por aderência, data e empresa.

### Dialogs e confirmações

Usar para: - Excluir dados ou documentos. - Descartar alterações não
salvas. - Retomar uma automação pausada após intervenção. - Confirmar
mudança de status feita manualmente.

Não solicitar confirmação repetida para ações reversíveis e rotineiras.

### Toasts e banners

-   Toast para sucesso breve ou falha recuperável.
-   Banner persistente para sessão expirada, intervenção necessária ou
    automação pausada.
-   Toda falha deve oferecer próximo passo sempre que possível.
-   Nunca mostrar segredos ou conteúdo pessoal desnecessário em
    notificações.

### Skeletons e carregamento

-   Usar skeletons para listas e cards.
-   Mostrar a etapa atual em tarefas demoradas.
-   Permitir navegar enquanto o processamento ocorre.
-   Distinguir "sem resultados" de "não foi possível consultar a fonte".

## 8. Padrões de tela

### Dashboard

Prioridade visual: 1. Estado da automação: ativa, pausada, aguardando
intervenção ou erro. 2. Resumo da última execução e próxima execução. 3.
Novas vagas e vagas com maior aderência. 4. Ações rápidas: "Buscar
agora", "Ver vagas", "Editar perfil".

Métricas sugeridas: novas vagas, vagas analisadas, currículos preparados
e tempo poupado estimado. O tempo poupado deve ser identificado como
estimativa, não medição garantida.

### Lista de vagas

-   Busca por texto.
-   Filtros por status, aderência, data, modalidade e empresa.
-   Ordenação.
-   Cards/lista com ações consistentes.
-   Estado vazio com botão para configurar ou executar busca.

### Detalhe da vaga

-   Cabeçalho com cargo, empresa e link de origem.
-   Resumo da vaga.
-   Aderência e explicação.
-   Requisitos atendidos, lacunas e dúvidas.
-   Ações: "Gerar currículo", "Marcar para revisar", "Arquivar".
-   Aviso quando a descrição estiver incompleta ou antiga.

### Editor de currículo

-   Coluna principal para editar conteúdo.
-   Painel secundário para requisitos da vaga e palavras-chave
    relevantes.
-   Comparação com currículo-base.
-   Aviso de conteúdo que não tem evidência no perfil.
-   Ações: salvar rascunho, pré-visualizar, exportar Markdown e exportar
    PDF.
-   Nunca substituir silenciosamente o currículo-base.

### Perfil

-   Seções estruturadas para resumo, experiências, formação,
    competências, projetos e idiomas.
-   Origem e confirmação de cada dado importado, quando aplicável.
-   Alertas para campos incompletos.
-   Possibilidade de editar e excluir dados.

### Automação

-   Frequência configurada: duas vezes por dia por padrão.
-   Horário da última e próxima execução.
-   Estado e duração da execução.
-   Botões de pausar, retomar e executar agora.
-   Lista de erros e intervenções pendentes.
-   Explicação clara de que automação de sites pode falhar ou depender
    de permissões e mudanças externas.

## 9. Acessibilidade

-   Contraste mínimo WCAG AA como meta.
-   Navegação completa por teclado.
-   Foco visível e não oculto.
-   Rótulos e mensagens de erro associados aos campos.
-   Ícones acompanhados de texto quando o significado não for universal.
-   Status comunicados por texto, não apenas por cor.
-   Respeitar preferência por movimento reduzido.
-   Não depender exclusivamente de gráficos para comunicar uma métrica.

## 10. Conteúdo e microcopy

Preferir frases concretas e honestas.

  -----------------------------------------------------------------------
  Situação                            Texto sugerido
  ----------------------------------- -----------------------------------
  Busca concluída                     "Busca concluída. 6 vagas novas
                                      foram adicionadas."

  Sem resultados                      "Nenhuma vaga nova foi encontrada
                                      com estes filtros."

  Fonte indisponível                  "Não foi possível consultar esta
                                      fonte. Você pode tentar novamente
                                      ou importar a vaga por URL."

  Sessão expirada                     "Sua sessão precisa de atenção.
                                      Abra o navegador, resolva o acesso
                                      e retome quando estiver pronto."

  Verificação detectada               "A automação foi pausada porque é
                                      necessária uma intervenção humana.
                                      Nenhuma candidatura foi enviada."

  Análise incompleta                  "A descrição não contém informação
                                      suficiente para avaliar todos os
                                      requisitos."

  Currículo pronto                    "Rascunho gerado. Revise os dados e
                                      as alterações antes de exportar."

  Campo não comprovado                "Esta informação não foi encontrada
                                      no seu perfil. Confirme ou remova
                                      antes de usar."

  Erro recuperável                    "A tarefa não foi concluída. Seus
                                      dados salvos foram preservados."
  -----------------------------------------------------------------------

## 11. Gráficos e visualização de dados

-   Usar gráficos somente quando ajudarem a identificar tendência ou
    distribuição.
-   Priorizar rótulos diretos e legendas claras.
-   Não usar gráficos de velocímetro para sugerir precisão artificial da
    aderência.
-   Em tendências semanais, mostrar período, unidade e fonte dos dados.
-   Disponibilizar os valores em formato textual ou tabular.

## 12. Tokens técnicos sugeridos

Exemplo de tokens CSS para implementação:

``` css
:root {
  color-scheme: dark;
  --color-bg-canvas: #101318;
  --color-bg-surface: #181D25;
  --color-bg-elevated: #202733;
  --color-border-default: #303947;
  --color-text-primary: #F2F5F9;
  --color-text-secondary: #A7B1C2;
  --color-text-muted: #7E899B;
  --color-brand-primary: #6C8CFF;
  --color-brand-secondary: #9B8AFB;
  --color-success: #46C99A;
  --color-warning: #F2B85B;
  --color-danger: #FF727F;
  --color-info: #63B8F5;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 18px;

  --font-sans: Inter, system-ui, "Segoe UI", sans-serif;
}
```

## 13. Critérios de aceite visual

-   A navegação principal é consistente em todas as telas.
-   Todas as ações têm estados de foco, hover, disabled e loading
    apropriados.
-   A aderência sempre vem acompanhada de explicação.
-   Estados vazios, erro, carregamento e intervenção humana estão
    desenhados.
-   O usuário consegue distinguir dados confirmados de inferências.
-   A interface nunca sugere que a candidatura foi enviada pelo agente.
-   O layout funciona em desktop e em janelas menores.
-   Componentes mantêm contraste e legibilidade.
-   O currículo pode ser revisado antes de exportar.
