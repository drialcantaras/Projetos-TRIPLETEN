<h1>Sprint 5 - Projeto (Ferramentas de Desenvolvimento de Softwares)</h1>

<h2>Descrição do projeto</h2>

O foco desse projeto é que você tenha mais prática com tarefas comuns de engenharia de software. Isso vai aprimorar e complementar suas habilidades de dados e vai fazer com que você seja uma opção mais atrativa para possíveis empregadores.

As tarefas são: criar e gerenciar ambientes virtuais de Python, desenvolver um aplicativo web e implantá-lo em um serviço de nuvem que o tornará acessível ao público.

Neste projeto, vamos fornecer um conjunto de dados de anúncios de vendas de carros. No entanto, neste projeto, o foco não será no conjunto de dados nem na análise, então você está livre para escolher o conjunto de dados que desejar.

<h2>Instruções para concluir o projeto</h2>

<h3>Etapa 1. Configurar tudo</h3>

1. Crie uma conta em github.com. Se você já tem uma conta ou criou uma no capítulo sobre o Git e GitHub, pode pular essa etapa.

2. Crie um novo repositório git com um arquivo README.md e um arquivo .gitignore (escolha um modelo de Python). Se precisar de uma recapitulação de como fazer isso, consulte esta lição.

3. Crie uma conta em render.com, se você ainda não fez isso. Falamos sobre o Render e aplicativos web nesta lição. Quando estiver criando uma conta no Render, selecione a opção "GitHub" e siga os passos para fazer sua inscrição. Isso é exatamente o que você precisa para vincular sua conta no Render à sua conta no GitHub.

4. Neste projeto, você vai realizar uma análise exploratória de dados. Para fazer isso, você precisa ter os pacotes pandas e plotly-express instalados. Já falamos sobre plotly nesta lição. plotly-express é projetado com padrões razoáveis e opções configuráveis para tipos comuns de gráficos, o que o torna um ótimo ponto de entrada para iniciantes, em comparação com o próprio plotly. Se ainda não o conhece bem, não se preocupe — vamos guiar você por todo o processo! Além disso, você vai precisar do pacote streamlit para desenvolver um aplicativo web. Crie um novo ambiente virtual e escolha um nome significativo que seja relacionado ao conjunto de dados com o qual você vai trabalhar. Por exemplo, você poderia chamá-lo de vehicles_env. Certifique-se de que você instalou pelo menos os seguintes pacotes no ambiente: pandas, streamlit e plotly-express.

5. Instale o VS Code, se você ainda não fez isso. Clone seu repositório do projeto do GitHub e abra-o como um projeto no VS Code. Esse será o diretório do seu projeto. Defina o interpretador Python para aquele usado pelo ambiente virtual que você criou anteriormente.

6. Para fins de simplicidade, em vez de salvar seu ambiente no arquivo requirements.txt no diretório do projeto, crie manualmente o arquivo requirement.txt e adicione três bibliotecas ali sem especificar as versões delas: pandas plotly_express streamlit

<h3>Etapa 2. Baixar o arquivo de dados</h3>

1. Baixe o conjunto de dados de anúncios de carros (vehicles_us.csv) ou encontre seu próprio conjunto de dados em formato CSV.

2. Coloque o conjunto de dados no diretório do projeto.

<h3>Etapa 3. Análise exploratória de dados</h3>

1. Crie um diretório chamado notebooks no diretório do seu projeto.

2. Crie um notebook Jupyter chamado EDA.ipynb no VS Code e salve-o no diretório notebooks do projeto. Lembre-se de que .ipynb é uma extensão de arquivo usada para notebooks Jupyter.

3. Abra o notebook Jupyter EDA.ipynb e faça testes com plotly-express para criar visualizações para uma análise exploratória básica do conjunto de dados no notebook.

<h3>Etapa 4. Desenvolver o dashboard do aplicativo web</h3>

1. Crie um arquivo app.py no diretório raiz do projeto. Para criar um arquivo .py, clique em "New File" (Novo arquivo) no VS Code e armazene-o no diretório do projeto com o nome desejado e a extensão .py.

2. Importe streamlit como st, pandas e plotly_express no início do arquivo.

3. Leia o arquivo CSV do conjunto de dados em um DataFrame. O código será o mesmo que você tinha no Jupyter Notebook ao explorar o conjunto de dados.

4. Agora, vamos criar o conteúdo do aplicativo baseado em Streamlit. Aqui está o que queremos que você inclua nele:
    - Pelo menos um cabeçalho. Você pode usar [st.header()] para fazer isso. Na lição sobre aplicativos web, mostramos como criar um cabeçalho.
    - Um botão que, ao ser clicado, cria um histograma plotly-express. Para fazer isso, considere usar as funções st.write() e st.plotly_chart() (os materiais estão em inglês). Aqui está um exemplo de como você pode fazer isso:

    import pandas as pd

    import plotly.express as px

    import streamlit as st
        
    car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

    hist_button = st.button('Criar histograma') # criar um botão
        
        if hist_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)


    - Adicione outro botão que, ao ser clicado, cria um gráfico de dispersão plotly-express. Сonsidere usar as funções st.write() e st.plotly_chart() (os materiais estão em inglês).


Esta etapa é opcional, mas, se você quiser um desafio extra, tente substituir botões por caixas de seleção, disponíveis em streamlit através de st.checkbox(). Você pode solicitar que o usuário selecione a caixa de seleção que corresponda a um histograma ou um gráfico de dispersão, e então um gráfico será criado dependendo da caixa selecionada. Aqui está um exemplo simples de como caixas de seleção funcionam em streamlit:
    import streamlit as st

        # criar uma caixa de seleção
        build_histogram = st.checkbox('Criar um histograma')

        if build_histogram: # se a caixa de seleção for selecionada
            st.write('Criando um histograma para a coluna odometer')
      ...

5. Certifique-se de atualizar o arquivo README quando terminar. Ele deve incluir uma breve descrição do projeto, explicando para que serve o aplicativo web e quais funcionalidades ele oferece.

6. Para tornar o Streamlit compatível com o Render, adicione um arquivo de configuração do Streamlit ao repositório do seu projeto em streamlit/config.toml com o seguinte conteúdo: toml [server] headless = true port = 10000 [browser] serverAddress = "0.0.0.0" serverPort = 10000 Ele dirá ao Render para procurar no lugar certo para ouvir seu aplicativo Streamlit ao colocá-lo em seus servidores.

7. Não se esqueça de confirmar e enviar todas as alterações de volta para o seu repositório após terminar o trabalho. Se você não fizer isso, nada vai funcionar direito.

**Observações importantes:**

- À medida que você desenvolve o aplicativo adicionando um novo componente Streamlit, você pode executar o comando streamlit run app.py do terminal para ver como está o resultado.
- À medida que você atinge alguns marcos no desenvolvimento do aplicativo (por exemplo, você adiciona um componente de trabalho e o aplicativo é executado sem erros), é uma boa prática fazer commit e enviar seu trabalho para um repositório remoto no GitHub. Portanto, não se esqueça de escrever uma mensagem de commit significativa!
- Abra sua conta em render.com e crie um novo serviço web:

1. Crie um novo serviço web vinculado ao seu repositório Github:

2. Configure o novo serviço web Render adicionando um comando de compilação Build Command que vai instalar tudo o que seja necessário para executar seu aplicativo, incluindo streamlit e todos os pacotes de requirements.txt. Use o seguinte comando:

- pip install --upgrade pip && pip install -r requirements.txt

Adicione o seguinte ao seu Start Command: streamlit run app.py.

3. Implemente o aplicativo no Render e aguarde até que a compilação seja bem-sucedida:

4. Verifique se seu aplicativo está acessível no seguinte URL: https://<APP_NAME>.onrender.com/

Observação: como você está usando uma versão gratuita, pode levar vários minutos após uma implementação bem-sucedida para que o aplicativo fique disponível online. Observe também que os aplicativos ficam "adormecidos" após ficarem inativos por alguns minutos. Nesse caso, basta carregar e atualizar a página do aplicativo algumas vezes para que ele seja ativado.

Se você atualizar seu repositório GitHub, para implementar a versão mais recente no Render, clique em Manual Deploy → Latest Commit.