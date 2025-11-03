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
st.header("O que você está procurando?")
opcoes = ["a) Projetos de Lei", "b) Propostas de Emenda Constitucional", "c) Deputados", "d) Sair"]
busca = st.radio("Selecione a opção da sua busca:", opcoes)
if busca == "a) Projetos de Lei":
  st.header("Você escolheu a opção de buscar projetos de lei.")
if busca == "b) Propostas de Emenda Constitucional":
  st.header("Você escolheu a opção de buscar propostas de emenda constitucional.")
if busca == "c) Deputados":
  st.header("Você escolheu a opção de buscar informações de deputados.")
if busca == "d) Sair":
  st.header("Você escolheu a opção de sair da pesquisa.")
  st.header("Obrigado por usar o programa. Até a próxima!")

#Resultado do Menu a) PL
if busca == "a) Projetos de Lei":
    numero_pl = st.text_input("Digite o número do projeto de lei:")
    ano_pl = st.text_input("Digite o ano do projeto de lei:")
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
                    st.header("Detalhes do Projeto")
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
                              st.header("Detalhes do Projeto")
                              st.write(f"Situação atual: {detalhes['statusProposicao']['descricaoSituacao']}")
                              st.write(f"Ementa completa: {detalhes['ementa']}")
                              st.write("Obrigado por usar o programa. Até a próxima!")
                          break
    else:
        st.write(f"Erro na requisição")

#Resultado Menu b) PEC
if busca == "b) Propostas de Emenda Constitucional":
    numero_pec = st.text_input("Digite o número da proposta de emenda constitucional:")
    ano_pec = st.text_input("Digite o ano da proposta de emenda constitucional:")
    url_busca_pec = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PEC&numero={numero_pec}&ano={ano_pec}"
    response_pec = requests.get(url_busca_pec)
    if response_pec.status_code == 200:
        dados_pec = response_pec.json()
        if dados_pec['dados']:
            for proposicao in dados_pec['dados']:
                  id_proposicao = proposicao['id']
                  st.header(f"PEC encontrada!")
                  url_detalhes = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes/{id_proposicao}"
                  response_detalhes = requests.get(url_detalhes)
                  if response_detalhes.status_code == 200:
                      detalhes = response_detalhes.json()['dados']
                      st.header("Detalhes da PEC")
                      st.write(f"Situação atual: {detalhes['statusProposicao']['descricaoSituacao']}")
                      st.write(f"Ementa completa: {detalhes['ementa']}")
                      st.write("Obrigado por usar o programa. Até a próxima!")
        else:
              while True:
                st.write(f"PEC {numero_pec}/{ano_pec} não encontrada.")
                numero_pec = st.text_input("Digite novamente o número da proposta de emenda constitucional: ")
                ano_pec = st.text_input("Digite novamente o ano da proposta de emenda constitucional: ")
                url_busca_pec = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PEC&numero={numero_pec}&ano={ano_pec}"
                response_pec = requests.get(url_busca_pec)
                if response_pec.status_code == 200:
                  dados_pec = response_pec.json()
                  if dados_pec['dados']:
                     for proposicao in dados_pec['dados']:
                       id_proposicao = proposicao['id']
                       st.header(f"PEC encontrado!")
                       url_detalhes = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes/{id_proposicao}"
                       response_detalhes = requests.get(url_detalhes)
                       if response_detalhes.status_code == 200:
                         detalhes = response_detalhes.json()['dados']
                         st.header("Detalhes da PEC")
                         st.write(f"Situação atual: {detalhes['statusProposicao']['descricaoSituacao']}")
                         at.write(f"Ementa completa: {detalhes['ementa']}")
                         st.write("Obrigado por usar o programa. Até a próxima!")
                       break
    else:
        st.write(f"Erro na requisição")

#Resultado do Menu c) Deputados
if busca == "c) Deputados":
    nome_deputado = st.text_input("Digite o nome do deputado(a):")
    url_deputados = f"https://dadosabertos.camara.leg.br/api/v2/deputados?nome={nome_deputado}"
    response = requests.get(url_deputados)
    if response.status_code == 200:
        dados_deputado = response.json()['dados']
        if dados_deputado:
            deputado_id = dados_deputado[0]['id']
            deputado_nome = dados_deputado[0]['nome']
            deputado_partido = dados_deputado[0]['siglaPartido']
            deputado_uf = dados_deputado[0]['siglaUf']
            df_deputado = pd.DataFrame(dados_deputado)
            st.header(f"Deputado(a) encontrado(a).")
            st.write(f"Nome: {deputado_nome}")
            st.write(f"Partido: {deputado_partido}")
            st.write(f"UF: {deputado_uf}")
            st.write(f"ID: {deputado_id}")
        else:
            while True:
              st.write(f"Nenhum deputado(a) encontrado com o nome '{nome_deputado}'.")
              nome_deputado = st.text_input("Digite o nome do deputado(a) novamente: ")
              url_deputados = f"https://dadosabertos.camara.leg.br/api/v2/deputados?nome={nome_deputado}"
              response = requests.get(url_deputados)
              if response.status_code == 200:
                dados_deputado = response.json()['dados']
                if dados_deputado:
                  deputado_id = dados_deputado[0]['id']
                  deputado_nome = dados_deputado[0]['nome']
                  deputado_partido = dados_deputado[0]['siglaPartido']
                  deputado_uf = dados_deputado[0]['siglaUf']
                  df_deputado = pd.DataFrame(dados_deputado)
                  st.header(f"Deputado(a) encontrado(a).")
                  st.write(f"Nome: {deputado_nome}")
                  st.write(f"Partido: {deputado_partido}")
                  st.write(f"UF: {deputado_uf}")
                  st.write(f"ID: {deputado_id}")
                break
    else:
        st.write(f"Erro na requisição")

#Menu c.1
if busca == "3" and response.status_code == 200 and dados_deputado:
            deputado_id = dados_deputado[0]['id']
            deputado_nome = dados_deputado[0]['nome']
            deputado_partido = dados_deputado[0]['siglaPartido']
            deputado_uf = dados_deputado[0]['siglaUf']
            df_deputado = pd.DataFrame(dados_deputado)
            st.header("O que mais você deseja saber a respeito desse deputado(a)?")
            opcoes_deputado = ["1 - Despesas do deputado(a)", "2 - Frentes parlamentares do deputado(a)", "3 - Órgão que o deputado(a) integra"]
            info_deputado = st.radio("Selecione a opção da sua busca:", opcoes_deputado)
            if info_deputado == "1 - Despesas do deputado(a)":
                st.header("Você escolheu a opção de buscar as despesas do deputado(a).")
                url_despesas = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas"
                response_despesas = requests.get(url_despesas)
                if response_despesas.status_code == 200:
                  dados_despesas = response_despesas.json()
                  df_despesas = pd.DataFrame(dados_despesas['dados'])
                  st.write(df_despesas.head())
                  st.write(f"Total de despesas: R$ {df_despesas['valorDocumento'].sum()}")
                  st.write("Obrigado por usar o programa. Até a próxima!")
                else:
                  st.write(f"Erro na requisição")
            elif info_deputado == "2 - Frentes parlamentares do deputado(a)":
                st.header("Você escolheu a opção de buscar as frentes parlamentares do deputado(a).")
                url_frentes = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/frentes"
                response_frentes = requests.get(url_frentes)
                if response_frentes.status_code == 200:
                  dados_frentes = response_frentes.json()
                  df_frentes = pd.DataFrame(dados_frentes['dados'])
                  st.write(df_frentes.head())
                  st.write("Obrigado por usar o programa. Até a próxima!")
                else:
                  st.write(f"Erro na requisição")
            elif info_deputado == "3":
                st.header("Você escolheu a opção de buscar os órgãos que o deputado(a) integra.")
                url_orgaos = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/orgaos"
                response_orgaos = requests.get(url_orgaos)
                if response_orgaos.status_code == 200:
                  dados_orgaos = response_orgaos.json()
                  df_orgaos = pd.DataFrame(dados_orgaos['dados'])
                  st.write(df_orgaos.head())
                  st.write("Obrigado por usar o programa. Até a próxima!")
                else:
                  st.write(f"Erro na requisição")
