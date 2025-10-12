import streamlit as st

st.title("Meu programa")
st.write("Alô mundo")

nome = st.text_input("Digite o seu nome: ")
if nome:
    st.write(nome.upper())

st.title("Lista de Exercícios 1")

st.write("1. A partir de um número informado pelo usuário, indique se um número inteiro qualquer é par ou ímpar.")
numero = int.text_input("Informe um número inteiro: "))
if numero % 2 == 0:
    st.text_input(f"O número {numero} é par.")
else:
    st.text_input(f"O número {numero} é ímpar.")
