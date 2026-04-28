<h1>Sprint 8 - Projeto (Introdução ao Aprendizado Automático)</h1>

<h2>Descrição do projeto</h2>

A operadora de celular Megaline está insatisfeita com o fato de muitos de seus clientes estarem usando planos antigos. Ela quer desenvolver um modelo que possa analisar o comportamento do cliente e recomendar um dos planos mais recentes da Megaline: Smart ou Ultra.

Você tem acesso a dados de comportamento dos clientes que já mudaram para os novos planos (do projeto do curso de Análise de dados estatísticos). Para essa tarefa de classificação, você precisa desenvolver um modelo que escolhe o plano certo. Como você já executou a etapa de pré-processamento de dados, pode ir direto para a criação do modelo.

Desenvolva um modelo com a maior acurácia possível. Neste projeto, o limite para acurácia é 0,75. Verifique a acurácia usando o conjunto de dados de teste.

<h2>Instruções do projeto</h2>

1. Abra e examine o arquivo de dados. Caminho para o arquivo: datasets/users_behavior.csv. Baixar o conjunto de dados
2. Divida os dados de origem em um conjunto de treinamento, um conjunto de validação e um conjunto de teste.
3. Investigue a qualidade de diferentes modelos alterando hiperparâmetros. Descreva brevemente os resultados do estudo.
4. Verifique a qualidade do modelo usando o conjunto de teste.
5. Tarefa adicional: tirar a prova real do modelo. Esses dados são mais complexos do que os que você está acostumado a trabalhar, então não será uma tarefa fácil. Vamos dar uma olhada mais de perto mais tarde.

<h2>Descrição de dados</h2>

Cada observação no conjunto de dados contém informações comportamentais mensais sobre um usuário. As informações dadas são as seguintes:

- сalls — número de chamadas
- minutes — duração total da chamada em minutos
- messages — número de mensagens de texto
- mb_used — Tráfego de internet usado em MB
- is_ultra — plano para o mês atual (Ultra - 1, Smart - 0)