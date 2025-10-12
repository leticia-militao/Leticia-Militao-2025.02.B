import streamlit as st

st.title("Meu programa")
st.write("Alô mundo")

nome = st.text_input("Digite o seu nome: ")
if nome:
    st.write(nome.upper())

st.title("Lista de Exercícios 1")

st.write("1. A partir de um número informado pelo usuário, indique se um número inteiro qualquer é par ou ímpar.")
numero = st.number_input("Informe um número inteiro: ")
if numero % 2 == 0:
    st.write(f"O número {numero} é par.")
else:
    st.write(f"O número {numero} é ímpar.")

st.write("2. Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota.")
nota1 = st.number_input("Informe a primeira nota: ")
nota2 = st.number_input("Informe a segunda nota: ")
nota3 = st.number_input("Informe a terceira nota: ")
nota4 = st.number_input("Informe a quarta nota: ")
notas = [nota1, nota2, nota3, nota4]
media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)
st.write(f"A média final é: {media}")
st.write(f"A maior nota é: {maior_nota}")
st.write(f"A menor nota é: {menor_nota}")

st.write("3. Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes.")
nome_completo = st.text_input("Informe o seu nome completo: ")
nomes = nome_completo.split()
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]
st.text_input(f"Primeiro nome: {primeiro_nome}")
st.text_input(f"Último nome: {ultimo_nome}")
