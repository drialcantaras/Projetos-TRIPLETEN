<h1>Sprint 13 - Projeto (Series Temporais)</h1>

<h2>Descrição do Projeto</h2>

A empresa Taxi Corrida Maluca coletou dados históricos sobre pedidos de táxi nos aeroportos. Para atrair mais motoristas durante o horário de pico, precisamos prever a quantidade de pedidos de táxi para a próxima hora. Construa um modelo para tal predição.

A métrica REQM no conjunto de teste não deve ser superior a 48.

**Instruções do projeto**

1. Faça download dos dados e faça uma nova amostragem deles de forma que cada ponto dos dados originais fique dentro de intervalos de uma hora.
2. Analise os dados.
3. Treine diferentes modelos com diferentes hiperparâmetros. A amostra de teste deve ser 10% do conjunto de dados inicial.
4. Teste os dados usando a amostra de teste e forneça uma conclusão.

**Descrição de dados**

Os dados são armazenados no arquivo /datasets/taxi.csv. Baixe o conjunto de dados. 

O número de pedidos está na coluna num_orders.