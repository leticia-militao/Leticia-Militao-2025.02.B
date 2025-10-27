#Configuração inicial do programa - importar bibliotecas necessárias
import requests
import json
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

#Apresentação
st.title("Câmara Aberta")
st.header("Uma plataforma dedicada ao acesso a informações da Câmara dos Deputados")
st.write("Aqui você pode buscar informações sobre Projetos de Lei, Propostas de Emenda Constitucional, ou deputados.")

#Menu 1 - Opção de Busca
st.write("O que você está procurando?")
opcoes = ["a) Projetos de Lei", "b) Propostas de Emenda Constitucional", "c) Deputados", "d) Sair"]
busca = st.radio("Selecione a opção da sua busca:", opcoes)
if busca == "a) Projetos de Lei":
  st.write("Você escolheu a opção de buscar projetos de lei.")
if busca == "b) Propostas de Emenda Constitucional":
  st.write("Você escolheu a opção de buscar propostas de emenda constitucional.")
if busca == "c) Deputados":
  st.write("Você escolheu a opção de buscar informações de deputados.")
if busca == "d) Sair":
  st.write("Você escolheu a opção de sair da pesquisa.")
  st.write("Obrigado por usar o programa. Até a próxima!")

#Resultado do Menu 1 - busca a) PL
if busca == "a) Projetos de Lei":
    numero_pl = st.text_input("Digite o número do projeto de lei:")
    ano_pl = st.text_input("Digite o ano do projeto de lei:")
    url_busca_pl = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PL&numero={numero_pl}&ano={ano_pl}"
    response_pl = requests.get(url_busca_pl)
    st.write(type(response_pl))
    if response_pl.ststus_code == 200:
        dados_pl = response_pl.json()
        if dados_pl['dados']:
            for proposicao in dados_pl['dados']:
                id_proposicao = proposicao['id']
                st.header(f"Projeto encontrado!")
                url_detalhes = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes/{id_proposicao}"
                response_detalhes = requests.get(url_detalhes)
                if response_detalhes.status_code == 200:
                    detalhes = response_detalhes.json()['dados']
                    st.header("--- Detalhes do Projeto ---")
                    st.write(f"Situação atual: {detalhes['statusProposicao']['descricaoSituacao']}")
                    st.write(f"Ementa completa: {detalhes['ementa']}")
                    st.write("Obrigado por usar o programa. Até a próxima!")
    else:
          while True:
              st.write(f"Projeto com o número {numero_pl} do ano {ano_pl} não encontrado.")
              numero_pl = st.text_input("Digite novamente o número do projeto de lei: ")
              ano_pl = st.text_input("Digite novamente o ano do projeto de lei: ")
              url_busca_pl = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PL&numero={numero_pl}&ano={ano_pl}"
              response_pl = requests.get(url_busca_pl)
              if response_pl.status_code == 200:
                  dados_pl = response_pl.json()
                  if dados_pl['dados']:
                      for proposicao in dados_pl['dados']:
                          id_proposicao = proposicao['id']
                          st.header(f"Projeto encontrado!")
                          url_detalhes = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes/{id_proposicao}"
                          response_detalhes = requests.get(url_detalhes)
                          if response_detalhes.status_code == 200:
                              detalhes = response_detalhes.json()['dados']
                              st.header("--- Detalhes do Projeto ---")
                              st.write(f"Situação atual: {detalhes['statusProposicao']['descricaoSituacao']}")
                              st.write(f"Ementa completa: {detalhes['ementa']}")
                              st.write("Obrigado por usar o programa. Até a próxima!")
