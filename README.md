# Financial_Health

# Documentação de criação do software.

## Objetivo: 
##### O objetivo deste documento é definir as informações e os requisitos necessários para criar um software que atenda às necessidades do cliente ou usuário final.
## Escopo:
##### O projeto se trata de um gerenciador financeiro de investimentos feitos. Investimentos tais como ações, FIs e Renda fixa dentre outros. O usuário poderá ter um melhor controle sobre seu patimônio, assim como métricas e desempenho de sua carteira no decorrer do tempo.  

## Definição de requesitos:

### 1. Requisitos Funcionais

**1.1 Cadastro de investimentos:** O programa deve permitir que o usuário cadastre investimentos de qualquer tipo, como ações, títulos, fundos imobiliários, fundos de investimento e outros tipos de investimentos.

**1.2 Monitoramento de investimentos:** O programa deve permitir que o usuário monitore o desempenho dos investimentos cadastrados, com informações atualizadas em tempo real, como valor atual, valorização, rentabilidade e outras informações relevantes.

**1.3 Análise de portfólio:** O programa deve permitir que o usuário visualize o desempenho geral do portfólio de investimentos, com informações sobre a distribuição de ativos, diversificação, risco e retorno.

**1.4 Ferramentas de análise:** O programa deve fornecer ferramentas para análise de investimentos, como gráficos, tabelas e relatórios, para que o usuário possa tomar decisões informadas sobre seus investimentos.


### 2. Requisitos Não Funcionais

**2.1 Interface intuitiva:** O programa deve ter uma interface fácil de usar e intuitiva para que o usuário possa navegar pelo programa facilmente.

**2.2 Segurança dos dados:** O programa deve ser seguro e proteger as informações do usuário, incluindo senhas, informações pessoais e informações de investimentos.

**2.3 Desempenho:** O programa deve ser rápido e confiável, com alta disponibilidade e tempos de resposta rápidos.

**2.4 Escalabilidade:** O programa deve ser escalável para lidar com um grande número de usuários e portfólios de investimento.

**2.5 Compatibilidade:** O programa deve ser compatível com diferentes dispositivos e sistemas operacionais, para que o usuário possa acessar o programa em qualquer dispositivo.

### 1. Caso de Uso: Cadastrar Investimento

Descrição: Este caso de uso permite ao usuário cadastrar um novo investimento no sistema.

Ator: Usuário

Pré-Condições:

O usuário deve estar logado no sistema.
Fluxo Básico:

O usuário clica no botão "Cadastrar Investimento" na interface do sistema.
O usuário preenche as informações do investimento, como nome do ativo, tipo de ativo, quantidade, valor da compra, entre outros.
O sistema verifica se todas as informações obrigatórias foram preenchidas corretamente.
O sistema armazena as informações do investimento na base de dados.
Fluxo Alternativo:
3.1 Se alguma informação obrigatória não for preenchida corretamente, o sistema apresenta uma mensagem de erro e solicita que o usuário corrija o campo específico.

### 2. Caso de Uso: Monitorar Investimento

Descrição: Este caso de uso permite ao usuário monitorar o desempenho de um investimento cadastrado no sistema.

Ator: Usuário

Pré-Condições:

O usuário deve estar logado no sistema.
O investimento a ser monitorado deve estar cadastrado no sistema.
Fluxo Básico:

O usuário clica no investimento que deseja monitorar na interface do sistema.
O sistema exibe as informações do investimento, como valor atual, valorização, rentabilidade e outras informações relevantes.
O usuário pode atualizar as informações do investimento clicando no botão "Atualizar".
Fluxo Alternativo:
2.1 Se as informações do investimento não puderem ser exibidas, o sistema apresenta uma mensagem de erro.

### 3. Caso de Uso: Analisar Portfólio

Descrição: Este caso de uso permite ao usuário visualizar e analisar o desempenho geral do portfólio de investimentos.

Ator: Usuário

Pré-Condições:

O usuário deve estar logado no sistema.
Fluxo Básico:

O usuário clica na opção "Analisar Portfólio" na interface do sistema.
O sistema exibe informações sobre a distribuição de ativos, diversificação, risco e retorno do portfólio do usuário.
O usuário pode usar ferramentas de análise, como gráficos, tabelas e relatórios, para avaliar o desempenho do portfólio.
Fluxo Alternativo:
2.1 Se as informações do portfólio não puderem ser exibidas, o sistema apresenta uma mensagem de erro.


- ### O projeto será desenvolvido de forma progressiva, onde cada fase do projeto será uma verão desse.

> ## Primeira fase:
- #### Nessa primeira fase será usado apenas recurssos básicos e sem GUI.
- #### Será criado um pequeno banco de dados num arquivo csv onde será armazenado as operaçoes feitas.
- ### Conteúdo do arquivo csv:
- Data da opereção
- Tipo do ativo
- Valor do ativo
- Valor da venda do ativo
- Nome do ativo
- Quantidade do ativo

- ### Operações realizaveis:
- Montante investido
- Montante total
- Rendimento por período
- Quantidade do ativo
- Porcentagem de cada ativo
- Porcentagem por tipo 
- Tempo como investidor


