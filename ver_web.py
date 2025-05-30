import streamlit as st
import re as r
from datetime import date
from minhafuncao import validar_email
from email_validator import EmailNotValidError

# Parte do nome.
st.title("Formulário para cadastro")

nome = st.text_input("Insira seu nome")

if st.button("Enviar"):
    if nome.strip() == '':
        st.warning("Insira seu nome")
    
    else:
        st.write(f"Seja bem-vindo {nome}")

# Sexo da pessoa
sexo = ("Masculino" , "Feminino" , "Prefiro não dizer")

opcoes = st.selectbox("Qual o seu sexo?", sexo)

if st.button("Envie"):
    if opcoes.strip() == '':
        st.warning("Informe seu sexo.")

    else:
        st.success("Informação Salva.")

# Data de nascimento da pessoa
st.title("Data de Nascimento")

min_data = date(1900, 1, 1) #valor minimo para inserir
max_data = date.today() 

# Pede a data de nascimento e limita para 2 paramentros, maximo e minimo que pode ter
data_de_nasc = st.date_input("Insira sua data de nascimento", min_value=min_data, max_value=max_data) 

if st.button("Verificar"):
    if data_de_nasc is None:
        st.warning("Insira sua data de nascimento.")

    else:
        st.success("Data de Nascimento salva")

# Parte do email
st.title("Email para contato.")

email = st.text_input("Insira seu Email.")

if st.button("Validar"):
    try:
        if validar_email(email):
            validacao_email = validar_email(email)
            st.success("Email cadastrado.")
        
        else:
            st.warning("Insira o seu Email.")

    except EmailNotValidError:
        st.warning("Insira o seu Email.") 

# Parte da profissão
st.title("Profissão")

profissoes = (
    "Administrador(a)",
    "Assistente Administrativo",
    "Analista Financeiro",
    "Contador(a)",
    "Economista",
    "Secretário(a)",
    "Recursos Humanos (RH)",
    "Professor(a)",
    "Pedagogo(a)",
    "Coordenador(a) Pedagógico(a)",
    "Diretor(a) Escolar",
    "Médico(a)",
    "Enfermeiro(a)",
    "Psicólogo(a)",
    "Dentista",
    "Fisioterapeuta",
    "Nutricionista",
    "Farmacêutico(a)",
    "Engenheiro(a) Civil",
    "Engenheiro(a) Elétrico(a)",
    "Engenheiro(a) Mecânico(a)",
    "Técnico(a) em Informática",
    "Técnico(a) em Eletrônica",
    "Desenvolvedor(a) de Software",
    "Analista de Sistemas",
    "Suporte Técnico",
    "Outros"
    )

profissao = st.selectbox("Qual é a sua profissão?", profissoes)

if st.button("Submit"):
    if profissao == '':
        st.warning("Escolha uma das profissões.")
    
    else:
        st.success("Profissão Salva.")

# Informações extras

interesse = st.text_input("Quais são os seus com a nossa empresa?")

if st.button("Submeter"):
    if interesse.strip() == '':
        st.warning("Digite seus interesses.")

    else:
        st.success("Interesses registrado.")

# Nota de satisfação
satisfeito = st.slider("Nota de satisfação", 1, 10, 5)

if st.button("Satisfação"):
    if satisfeito <= 4:
        st.write("Obrigado pela avaliação, iremos melhorar para formulários futuros.")

    else:
        st.write("Obrigado pela avaliação, sua avaliação é importante para nós.")