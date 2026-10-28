# JobMatch Agent --- PRD

**Versão:** 1.0\
**Status:** Proposta reconstruída a partir das decisões já discutidas\
**Produto:** Assistente pessoal de busca e preparação de candidaturas
com IA\
**Abordagem:** Local-first, human-in-the-loop

## 1. Visão do produto

O JobMatch Agent ajuda o candidato a encontrar vagas relevantes,
entender o quanto seu perfil combina com cada oportunidade e preparar
materiais de candidatura personalizados. O agente automatiza pesquisa,
organização e preparação, mas mantém o usuário no controle das decisões
importantes.

O MVP começa pelo LinkedIn e executa localmente no computador do
usuário, usando uma sessão de navegador autenticada pelo próprio
usuário. A pesquisa é agendada duas vezes ao dia.

### Problema

A busca por emprego envolve tarefas repetitivas: encontrar vagas,
comparar requisitos, adaptar currículo, registrar candidaturas e
preencher formulários. Isso consome tempo e torna difícil manter
consistência entre oportunidades.

### Proposta de valor

-   Reduzir a preparação de uma candidatura de aproximadamente 45
    minutos para menos de 3 minutos, quando a vaga e os dados
    necessários estiverem acessíveis.
-   Priorizar vagas com maior aderência ao perfil.
-   Produzir currículos direcionados à vaga, sem inventar experiências
    ou competências.
-   Manter histórico rastreável da busca e das decisões.
-   Deixar a candidatura final sob controle humano.

## 2. Objetivos e métricas

### Objetivos do MVP

1.  Capturar vagas a partir de buscas configuradas no LinkedIn.
2.  Evitar registros duplicados e manter o status de cada oportunidade.
3.  Comparar requisitos da vaga com o perfil profissional do usuário.
4.  Explicar a pontuação de aderência com evidências.
5.  Gerar currículo personalizado em Markdown e PDF.
6.  Preparar dados para preenchimento de formulário quando possível, sem
    enviar a candidatura.
7.  Interromper o fluxo e solicitar intervenção humana diante de
    CAPTCHA, verificação, login expirado ou qualquer obstáculo
    inesperado.

### Métricas de sucesso

-   Tempo mediano para preparar currículo e resumo de candidatura:
    **menos de 3 minutos** após a vaga ser processada.
-   Percentual de vagas processadas sem duplicação: **≥ 95%** nas fontes
    e condições suportadas.
-   Toda recomendação de aderência deve conter justificativas e lacunas
    identificadas.
-   **Zero candidaturas enviadas automaticamente** pelo agente.
-   **Zero competências ou experiências inventadas** nos documentos
    gerados.
-   O usuário consegue pausar a automação e revisar ou excluir dados
    locais.

As métricas são metas iniciais, não resultados já comprovados.

## 3. Público e cenário principal

**Usuário principal:** candidato que busca vagas de desenvolvimento de
software e quer reduzir trabalho manual sem abrir mão do controle sobre
a candidatura.

**Cenário principal:** 1. O usuário configura perfil, currículo-base,
cargos-alvo, localização/remoto e filtros. 2. O agente executa uma busca
agendada no LinkedIn duas vezes por dia. 3. As vagas encontradas são
normalizadas e deduplicadas. 4. O sistema extrai requisitos acessíveis e
calcula uma análise de aderência. 5. O usuário consulta uma lista
ordenada, filtra e abre uma vaga. 6. O agente gera um currículo
direcionado e um resumo de candidatura. 7. Se o usuário optar por
iniciar o preenchimento assistido, o agente preenche apenas campos que
consegue identificar com segurança. 8. O usuário revisa tudo e realiza
manualmente o envio final. 9. O histórico registra o que foi encontrado,
gerado, revisado e alterado.

## 4. Escopo do MVP

### Incluído

-   Execução local no computador do usuário.
-   Configuração de perfil profissional e currículo-base.
-   Definição de termos de busca, cargos, localidade, modalidade
    remota/híbrida/presencial e filtros básicos.
-   Busca no LinkedIn duas vezes ao dia, conforme limites técnicos e
    regras aplicáveis.
-   Importação manual por URL como alternativa quando a automação não
    funcionar.
-   Extração de título, empresa, localidade, data, descrição e URL,
    quando disponíveis.
-   Deduplicação por URL normalizada e identificadores disponíveis.
-   Lista de vagas com status e filtros.
-   Análise de aderência baseada em critérios explícitos.
-   Identificação de competências correspondentes, requisitos ausentes e
    pontos a confirmar.
-   Geração de currículo personalizado em Markdown e PDF.
-   Geração de resumo de candidatura e sugestões de respostas
    fundamentadas no perfil.
-   Preparação assistida de campos de formulário, sem envio final.
-   Pausa, retomada e execução manual.
-   Logs locais e tratamento de erros.
-   Configuração de provedor/modelo de IA e limites de uso, quando
    viável.

### Fora do escopo inicial

-   Envio automático de candidaturas.
-   Contornar CAPTCHA, autenticação multifator, filas, controles
    anti-bot ou outras medidas de segurança.
-   Aplicar automaticamente em massa.
-   Garantir pontuação ou aprovação em sistemas ATS específicos.
-   Suporte completo a LinkedIn, Gupy, Indeed e outras plataformas desde
    o primeiro lançamento.
-   Extensão de navegador ou serviço hospedado na nuvem.
-   Treinar um modelo próprio.
-   Enviar mensagens automáticas a recrutadores.
-   Tomar decisões de candidatura sem revisão do usuário.

## 5. Requisitos funcionais

### RF-01 --- Perfil do candidato

O usuário pode manter: - Nome e dados de contato que deseje incluir. -
Resumo profissional. - Experiências, projetos, formação e
certificações. - Competências técnicas e comportamentais. - Idiomas e
nível informado. - Preferências de trabalho e cargos-alvo. - Restrições
ou informações que não devem ser incluídas em currículos.

O sistema deve tratar o perfil como fonte de verdade. Se uma informação
não existir, deve pedir confirmação ou omiti-la --- nunca inventá-la.

### RF-02 --- Currículo-base

O usuário pode importar ou colar seu currículo-base, revisar os dados
extraídos e editar as informações estruturadas. O documento original
deve ser preservado sem alterações automáticas.

### RF-03 --- Configuração de busca

O usuário pode configurar: - Palavras-chave e cargos. - Localidade e
raio, se aplicável. - Remoto, híbrido ou presencial. - Senioridade e
tipo de contrato, quando os dados estiverem disponíveis. - Frequência:
duas execuções diárias por padrão. - Termos a incluir ou excluir.

A interface deve mostrar a última execução, a próxima execução prevista
e o estado do agendamento.

### RF-04 --- Coleta e importação de vagas

O sistema deve: - Obter somente dados que estejam acessíveis por meios
permitidos e tecnicamente suportados. - Armazenar a URL de origem e a
data/hora da captura. - Registrar campos indisponíveis sem preencher
valores fictícios. - Permitir adicionar uma vaga manualmente por URL ou
texto. - Exibir aviso quando a descrição estiver incompleta ou
desatualizada.

**Nota de viabilidade:** a disponibilidade de APIs oficiais e as
permissões para automação variam. O MVP deve verificar os termos atuais
da plataforma e preferir interfaces oficiais quando disponíveis. Não
deve tentar contornar controles de acesso. Se a automação de navegador
não for permitida ou confiável, usar importação manual/assistida como
fallback.

### RF-05 --- Deduplicação

Considerar duplicadas vagas com a mesma URL canônica ou identificador de
origem. Como fallback, comparar empresa, título e localidade. Quando
houver dúvida, sinalizar possível duplicata em vez de excluir
silenciosamente.

### RF-06 --- Análise de aderência

Cada vaga processada deve apresentar: - Pontuação de aderência de 0 a
100, acompanhada de explicação. - Requisitos obrigatórios
identificados. - Competências do perfil que correspondem aos
requisitos. - Lacunas ou requisitos não comprovados. - Palavras-chave
relevantes para currículo. - Grau de confiança e campos da descrição que
faltam. - Recomendação explicável, nunca uma decisão automática de
candidatura.

A pontuação deve ser heurística e transparente. Não deve ser apresentada
como probabilidade de contratação ou como pontuação real de ATS.

### RF-07 --- Currículo personalizado

O usuário pode gerar uma versão direcionada para uma vaga em Markdown e
PDF. O agente pode reorganizar e enfatizar informações existentes,
adequar linguagem e incluir palavras-chave verdadeiras. Não pode
inventar experiências, resultados, anos de experiência, certificações,
domínio de ferramentas ou métricas.

Antes da exportação, mostrar comparação com o currículo-base e permitir
edição. O currículo-base nunca deve ser sobrescrito.

### RF-08 --- Resumo de candidatura

Gerar um resumo curto da vaga, motivos de aderência, lacunas,
palavras-chave importantes e perguntas que o candidato deve confirmar.
Respostas sugeridas para formulários devem ser fundamentadas no perfil e
marcadas para revisão.

### RF-09 --- Preenchimento assistido

Quando tecnicamente suportado, o agente pode preparar ou preencher
campos identificados com segurança. Antes de interagir, deve mostrar o
que pretende preencher quando a ação tiver consequências relevantes. Não
deve clicar no botão final de envio nem confirmar candidatura.

Se houver CAPTCHA, verificação de identidade, login expirado, desafio
anti-bot ou campo ambíguo, pausar e pedir que o usuário intervenha. Após
a intervenção, só continuar quando o usuário retomar explicitamente.

### RF-10 --- Status e histórico

Estados sugeridos para uma vaga: - Nova - Analisada - Revisar -
Currículo preparado - Candidatura em preparação - Candidatura enviada
pelo usuário - Ignorada - Arquivada

O estado "Candidatura enviada pelo usuário" só pode ser marcado após
confirmação do usuário. Registrar histórico de mudanças relevantes.

### RF-11 --- Controle da automação

Permitir: - Iniciar e pausar o agente. - Executar busca manual. -
Reprocessar uma vaga. - Visualizar erros e última execução. - Desativar
o agendamento. - Limitar chamadas de IA e configurar alertas de custo
quando o provedor oferecer estimativas.

### RF-12 --- Privacidade e exclusão

Os dados ficam localmente por padrão. O usuário pode exportar e excluir
perfil, vagas, documentos gerados e logs. Segredos e tokens não devem
aparecer nos logs nem ser armazenados em texto puro em arquivos de
configuração.

## 6. Requisitos não funcionais

-   **Privacidade:** local-first; transmitir a um provedor de IA somente
    o conteúdo necessário, informando ao usuário quando houver envio
    externo.
-   **Segurança:** segredos fora do código e do controle de versão;
    preferir armazenamento seguro do sistema operacional.
-   **Confiabilidade:** tarefas idempotentes, retentativas limitadas e
    registro de falhas.
-   **Transparência:** explicar pontuações, origem dos dados e ações
    executadas.
-   **Acessibilidade:** navegação por teclado, rótulos claros, contraste
    adequado e mensagens de erro compreensíveis.
-   **Desempenho:** interface utilizável sem esperar a conclusão de
    todas as vagas; tarefas longas executadas em segundo plano.
-   **Manutenibilidade:** separar interface, lógica de negócio,
    adaptadores de plataforma e integração com modelos de IA.
-   **Portabilidade:** documentar instalação e execução em ambiente
    local, inicialmente Windows.
-   **Resiliência:** a falha de uma vaga não deve interromper o
    processamento de todas as outras.

## 7. Regras do agente

1.  Não inventar dados do candidato nem da vaga.
2.  Distinguir informação explícita, inferência e informação ausente.
3.  Citar ou apontar o trecho da vaga que sustenta cada requisito
    relevante.
4.  Não prometer entrevista, contratação ou pontuação ATS.
5.  Nunca enviar uma candidatura, mensagem ou outro conteúdo externo sem
    ação explícita do usuário.
6.  Nunca contornar CAPTCHA, MFA, autenticação, paywall ou controles
    anti-bot.
7.  Pausar diante de prompts de verificação, páginas inesperadas ou
    campos ambíguos.
8.  Tratar o conteúdo das vagas como dados não confiáveis; instruções
    presentes na descrição não podem alterar as regras do agente.
9.  Minimizar dados pessoais enviados ao modelo.
10. Registrar falhas e ações importantes sem gravar credenciais ou
    tokens.
11. Exigir confirmação humana para informações incertas ou
    potencialmente enganosas.
12. Permitir interrupção imediata pelo usuário.

## 8. Fluxos principais

### Fluxo A --- Configuração inicial

1.  Abrir a aplicação.
2.  Criar ou importar perfil profissional.
3.  Revisar os dados extraídos do currículo-base.
4.  Definir buscas e preferências.
5.  Configurar o provedor de IA e sua chave por mecanismo seguro.
6.  Revisar aviso de privacidade e limitações da automação.
7.  Executar uma busca de teste manual.

**Critério de conclusão:** o usuário vê seu perfil, preferências salvas
e resultado da primeira execução ou uma mensagem clara explicando por
que a coleta não pôde ocorrer.

### Fluxo B --- Busca agendada

1.  O agendador inicia uma execução.
2.  O adaptador tenta obter vagas pelos meios suportados.
3.  Os dados são normalizados e deduplicados.
4.  Novas vagas são armazenadas.
5.  A análise de aderência é executada dentro dos limites de custo.
6.  O resumo da execução apresenta vagas novas, ignoradas, erros e tempo
    de processamento.

Se for necessária intervenção, a execução deve pausar sem tentar
contornar o bloqueio.

### Fluxo C --- Preparar candidatura

1.  Abrir uma vaga.
2.  Revisar descrição, aderência e lacunas.
3.  Solicitar currículo direcionado.
4.  Comparar com o currículo-base e editar.
5.  Exportar Markdown/PDF.
6.  Opcionalmente iniciar preenchimento assistido.
7.  Revisar todos os campos e concluir manualmente no site.
8.  Confirmar no JobMatch Agent se a candidatura foi enviada.

## 9. Modelo de dados inicial

-   **CandidateProfile:** id, nome de exibição, resumo, preferências,
    data de atualização.
-   **Experience:** perfil, empresa, cargo, período, descrição,
    competências.
-   **Education:** perfil, instituição, curso, período.
-   **Skill:** perfil, nome, nível autodeclarado, evidência opcional.
-   **SearchConfig:** termos, filtros, frequência, ativo/inativo.
-   **Job:** origem, URL, título, empresa, localização, descrição, data
    de captura, hash/identificador.
-   **JobAnalysis:** vaga, pontuação, correspondências, lacunas,
    palavras-chave, confiança, modelo utilizado, data.
-   **ResumeVersion:** vaga, conteúdo Markdown, caminho do PDF, data,
    revisão.
-   **ApplicationActivity:** vaga, status, timestamp, ação, confirmação
    do usuário.
-   **RunLog:** execução, início/fim, status, contagens, erros
    sanitizados.

Para o MVP, **PostgreSQL é o banco de dados adotado**, garantindo suporte a concorrência, integridade relacional e escalabilidade desde o início, mantendo a camada de acesso isolada por repositórios/ORM.

## 10. Arquitetura proposta

### Componentes

-   **Frontend:** React + TypeScript, interface local.
-   **Backend:** Python + FastAPI, API e regras de negócio.
-   **Persistência:** PostgreSQL no MVP, com camada de acesso isolada (repositórios/ORM).
-   **Agendador:** processo local com execução duas vezes ao dia e botão
    para execução manual.
-   **Adaptador de vagas:** integração separada por plataforma; LinkedIn
    primeiro, com fallback de importação manual.
-   **Camada de IA:** interface de provedor independente; Google ADK
    pode ser avaliado para orquestração, sem tornar o restante do
    sistema dependente dele.
-   **Documentos:** Markdown como formato intermediário e geração de PDF
    a partir dele.
-   **Automação de navegador:** sessão local autenticada, apenas em
    fluxos permitidos e com limites claros.
-   **Observabilidade:** logs estruturados locais, sem segredos.

### Princípios

-   Lógica de negócio não deve depender diretamente do DOM do LinkedIn
    ou de um fornecedor de LLM.
-   Adaptadores devem ter limites, timeout, retentativas e tratamento de
    erro.
-   Processamento de vagas deve ser idempotente.
-   A geração de currículo deve poder ser testada sem abrir o navegador.
-   Agendamento não deve depender de uma aba da interface permanecer
    aberta; a estratégia exata deve ser validada no sistema operacional
    alvo.

## 11. Interface e telas

1.  **Dashboard:** resumo da última busca, próximas execuções, novas
    vagas e alertas.
2.  **Vagas:** lista pesquisável com filtros por aderência, data,
    empresa e status.
3.  **Detalhe da vaga:** descrição, requisitos, análise, lacunas e
    ações.
4.  **Currículo:** comparação lado a lado com currículo-base, editor e
    exportação.
5.  **Perfil:** experiências, competências, formação e currículo-base.
6.  **Buscas e automação:** filtros, frequência, estado, execução manual
    e pausa.
7.  **Histórico e configurações:** logs sanitizados, provedor de IA,
    limites, privacidade e exclusão de dados.

## 12. Critérios de aceite do MVP

-   O usuário consegue criar/editar seu perfil e preservar o
    currículo-base.
-   O usuário consegue configurar ao menos uma busca e executá-la
    manualmente.
-   O sistema consegue importar uma vaga por URL ou texto quando a
    coleta automatizada falhar.
-   Vagas repetidas não são duplicadas silenciosamente.
-   A análise mostra correspondências, lacunas e justificativas.
-   O currículo direcionado pode ser editado e exportado em Markdown e
    PDF.
-   O agente não inclui fatos profissionais sem evidência no perfil.
-   A execução agendada pode ser pausada e reativada.
-   Diante de verificação, bloqueio ou ambiguidade, o agente pausa e
    pede intervenção.
-   Não existe ação automática de envio final.
-   O usuário consegue ver erros e excluir os dados locais.
-   Segredos não aparecem nos logs nem no repositório.

## 13. Riscos e mitigação

  -----------------------------------------------------------------------
  Risco                               Mitigação
  ----------------------------------- -----------------------------------
  Mudanças na interface do LinkedIn   Adaptador isolado, testes manuais e
                                      importação por URL/texto como
                                      fallback

  Restrições de termos de uso         Verificar regras atuais antes de
                                      automatizar; não contornar
                                      controles; oferecer fluxo manual

  Dados incompletos ou desatualizados Mostrar fonte, data de captura e
                                      campos ausentes

  Alucinações do modelo               Fundamentar saídas no perfil e na
                                      vaga; revisão humana; validações

  Custo variável de IA                Limites por execução, modelo
                                      econômico para triagem e
                                      configuração de orçamento

  Vazamento de dados                  Armazenamento local, minimização de
                                      dados e proteção de credenciais

  PDF mal formatado                   Visualização prévia e teste com
                                      currículos de tamanhos diferentes

  Agendamento não executado           Mostrar última execução, erros e
                                      instruções para manter o serviço
                                      local ativo
  -----------------------------------------------------------------------

## 14. Plano de implementação

### Fase 1 --- Fundação

-   Repositório, ambiente local e configuração.
-   Modelos de dados e PostgreSQL com migrações.
-   Perfil do candidato e currículo-base.
-   Estrutura visual e navegação principal.

### Fase 2 --- Vagas

-   Cadastro/importação manual.
-   Lista e detalhe da vaga.
-   Normalização e deduplicação.
-   Status e histórico.

### Fase 3 --- Análise com IA

-   Extração estruturada de requisitos.
-   Comparação com perfil.
-   Pontuação explicável e lacunas.
-   Testes contra dados ausentes e instruções maliciosas em descrições.

### Fase 4 --- Currículo

-   Geração de Markdown.
-   Editor e comparação com o currículo-base.
-   Exportação PDF e validação visual.

### Fase 5 --- Busca assistida

-   Validar o método permitido de coleta no LinkedIn.
-   Criar adaptador isolado.
-   Tratamento de sessão expirada e bloqueios.
-   Importação manual como fallback confiável.

### Fase 6 --- Agendamento e preparação

-   Execução duas vezes ao dia.
-   Logs, pausa, retomada e limites de custo.
-   Preenchimento assistido opcional sem envio final.
-   Testes de aceitação e documentação de instalação.

## 15. Decisões em aberto

-   Provedor e modelo de IA iniciais.
-   Método exato de coleta de vagas compatível com as regras atuais do
    LinkedIn.
-   Estratégia de execução em segundo plano no Windows.
-   Biblioteca de exportação PDF.
-   Se a primeira versão usará apenas importação manual até validar a
    automação.
-   Quais dados do candidato serão enviados ao provedor de IA e quais
    devem ser mascarados.

Estas decisões devem ser fechadas antes de implementar os adaptadores
externos, não precisam bloquear o desenvolvimento do núcleo local.