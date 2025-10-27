import requests
import json
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Câmara Aberta")
st.header("Uma plataforma dedicada ao acesso a informações da Câmara dos Deputados")
st.write("Que tipo de busca você deseja fazer?")
st. write("1 - Projetos de Lei")
st. write("2 - Propostas de Emenda Constitucional")
st. write("3 - Deputados")
st. write("4 - Sair")
busca = st.text_input("Digite o número da opção da sua busca:")
