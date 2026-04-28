import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title('Análise de Anúncios de Veículos - EUA')

# Carregar dados
df = pd.read_csv('vehicles_us.csv')

# Exibir amostra
st.subheader('Visualização dos dados')
st.dataframe(df.head())

# Gráfico de dispersão
st.subheader('Relação entre preço e ano do modelo')
fig = px.scatter(df, x='model_year', y='price', color='type', title='Preço vs Ano do Modelo')
st.plotly_chart(fig)

# Estatísticas simples
st.subheader('Resumo estatístico')
st.write(df.describe())
