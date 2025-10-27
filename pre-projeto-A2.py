import requests
import json
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Câmara Aberta")
st.header("Uma plataforma dedicada ao acesso a informações da Câmara dos Deputados")
st.write("Que tipo de busca você deseja fazer?")
opcoes = ["1 - Projetos de Lei", "2 - Propostas de Emenda Constitucional", "3 - Deputados", "4 -  Sair"]
busca = st.radio("Digite o número da opção da sua busca:", opcoes)
st.write("Você escolheu: {busca}")
