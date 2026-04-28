<h1>Sprint 11 - Projeto (Álgebra Linear)</h1>
<h2>Descrição do Projeto</h2>

<strong>Tarefa 1:</strong> Encontrar clientes semelhantes a um determinado cliente. Isso vai ajudar os agentes da empresa com tarefas de marketing.

<strong>Tarefa 2:</strong> Predizer se um novo cliente provavelmente receberá um pagamento de seguro. Um modelo de predição pode ser melhor do que um modelo dummy?

<strong>Tarefa 3:</strong> Predizer o número de pagamentos de seguro que um novo cliente provavelmente receberá usando um modelo de regressão linear.

<strong>Tarefa 4:</strong> Proteger os dados pessoais dos clientes sem prejudicar o modelo da tarefa anterior.

É necessário desenvolver um algoritmo de transformação de dados que tornaria difícil recuperar informações pessoais se os dados caíssem nas mãos erradas. Isso é chamado de mascaramento de dados ou ofuscação de dados. Mas os dados devem ser protegidos de forma que a qualidade dos modelos de aprendizado de máquina não piore. Você não precisa escolher o melhor modelo, só prove que o algoritmo funciona corretamente.

<h2>Instruções do Projeto</h2>

1. Carregue os dados.
2. Verifique se os dados estão livres de problemas — não há dados ausentes, valores extremos e assim por diante.
3. Trabalhe em cada tarefa e responda às perguntas feitas no modelo de projeto.
4. Tire conclusões com base em sua experiência trabalhando no projeto.
5. Há algum pré-código no modelo do projeto, sinta-se à vontade para usá-lo, alguns deles precisam ser concluídos primeiro. Além disso, há dois apêndices no modelo de projeto com informações úteis.

<h2>Descrição de Dados</h2>

O conjunto de dados é armazenado no arquivo /datasets/insurance_us.csv. Você pode baixar o conjunto de dados aqui.

Características (_features_): sexo, idade, salário e número de familiares do segurado.

Alvo (_target_): número de pagamentos de seguro recebidos por um segurado nos últimos cinco anos.