import requests
import json
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Câmara Aberta")
st.subtitle("Uma plataforma dedicada ao acesso a informações da Câmara dos Deputados")
st.write("Que tipo de busca você deseja fazer?
         1 - Projetos de Lei
         2 - Propostas de Emenda Constitucional
         3 - Deputados
         4 - Sair")
busca = st.text_input("Digite o número da opção da sua busca:")
