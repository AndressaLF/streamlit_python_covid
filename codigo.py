
import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('covid-variants.csv')

paises = list(df['location'].unique())
variantes = list(df['variant'].unique())

df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

pais = st.sidebar.selectbox('Escolha o país', ['Todos'] + paises)
variante = st.sidebar.selectbox('Escolha a variante', ['Todas'] + variantes)


if (pais != 'Todos'):
    st.header('Mostrando resultado de ' + pais)
    df = df[df['location'] == pais]
else:
    st.header('Mostrando resultado para todos os países')
    
if (variante != 'Todas'):
    st.subheader('Mostrando resultado para variante ' + variante)
    df = df[df['variant'] == variante]
else:
    st.subheader('Mostrando resultado para todas as variantes')


dfShow = df.groupby(by = ['date']).sum()

fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title='Casos Diários de Covid-19')
st.plotly_chart(fig, use_container_width=True)