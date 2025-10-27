import requests
import json
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Câmara Aberta")
st.header("Uma plataforma dedicada ao acesso a informações da Câmara dos Deputados")
st.write("Que tipo de busca você deseja fazer?")
opcoes = ["1 - Projetos de Lei", "2 - Propostas de Emenda Constitucional", "3 - Deputados", "4 - Sair"]
busca = st.radio("Digite o número da opção da sua busca:", opcoes)
if busca == "1 - Projetos de Lei":
  st.write("Você escolheu a opção de buscar projetos de lei.")
if busca == "2 - Propostas de Emenda Constitucional":
  st.write("Você escolheu a opção de buscar propostas de emenda constitucional.")
if busca == "3 - Deputados":
  st.write("Você escolheu a opção de buscar informações de deputados.")
if busca == "4 - Sair":
  st.write("Você escolheu a opção de sair da pesquisa.")
  st.write("Obrigado por usar o programa. Até a próxima!")
