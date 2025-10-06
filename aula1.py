import streamlit as st

st.title("Meu programa")
st.write("Alô mundo")

nome = st.text_input("Digite o seu nome: ")
if nome:
    st.writite(nome.upper())
