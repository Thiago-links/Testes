import streamlit as st
import re as r
from datetime import date
from minhafuncao import validar_email
from email_validator import EmailNotValidError

# Parte do nome.
st.title("Formulário para cadastro")

st.subheader("Nome")
nome = st.text_input("Insira seu nome")

# Sexo da pessoa
st.subheader("Sexo")
sexo = ("Masculino" , "Feminino" , "Prefiro não dizer")

opcoes = st.selectbox("Qual o seu sexo?", sexo)

# Data de nascimento da pessoa
st.subheader("Nascimento")

min_data = date(1900, 1, 1) #valor minimo para inserir
max_data = date.today() 

# Pede a data de nascimento e limita para 2 paramentros, maximo e minimo que pode ter
data_de_nasc = st.date_input("Insira sua data de nascimento", min_value=min_data, max_value=max_data) 

# Parte do email
st.subheader("Email para contato.")

email = st.text_input("Insira seu Email.")

if st.button("Validar"):
    try:
        if validar_email(email):
            validacao_email = validar_email(email)
            st.success("Email salvo.")
        
        else:
            st.warning("Insira o seu Email.")

    except EmailNotValidError:
        st.warning("Insira o seu Email.") 

# Parte da profissão
st.subheader("Profissão")

profissoes = (
    "Estudante", "Administrador(a)", "Assistente Administrativo", "Analista Financeiro", "Contador(a)",
    "Economista", "Secretário(a)","Recursos Humanos (RH)","Professor(a)","Pedagogo(a)",
    "Coordenador(a) Pedagógico(a)","Diretor(a) Escolar","Médico(a)","Enfermeiro(a)","Psicólogo(a)",
    "Dentista","Fisioterapeuta","Nutricionista","Farmacêutico(a)","Engenheiro(a) Civil",
    "Engenheiro(a) Elétrico(a)","Engenheiro(a) Mecânico(a)","Técnico(a) em Informática","Técnico(a) em Eletrônica",
    "Desenvolvedor(a) de Software","Analista de Sistemas","Suporte Técnico",
    "Outros"
    )

profissao = st.selectbox("Qual é a sua profissão?", profissoes)

# Informações extras
st.subheader("Interesse")

interesse = st.text_input("Quais são os seus interesses com a nossa empresa?")

# Nota de satisfação
st.subheader("Avaliação")

satisfeito = st.slider("Nota de satisfação", 0, 10, 0)

if st.button("Satisfação"):
    if satisfeito <= 4:
        st.write("Obrigado pela avaliação, iremos melhorar para formulários futuros.")

    else:
        st.write("Obrigado pela avaliação, sua avaliação é importante para nós.")

if st.button("Enviar Formulário completo"):

    if nome.strip() == '':
        st.warning("Insira seu nome")
    
    elif data_de_nasc > date(2015,5,25):
        st.warning("Idade Inválida")

    elif email.strip() == '':
        st.warning("Insira seu Email")
    
    elif '@' not in email or '.com' not in email:
        st.warning("O Email deve conter @,  .com")

    elif interesse.strip() == '':
        st.warning("Digite seus interesses")

    else:
        dados = (
        f"Nome: {nome}\n"
        f"Sexo: {opcoes}\n"
        f"Data de Nascimento: {data_de_nasc}\n"
        f"Email: {email}\n"
        f"Profissão: {profissao}\n"
        f"Interesse: {interesse}\n"
        f"Nota de Satisfação: {satisfeito}\n"
        f"{'-'*50}\n"
        )
        with open('dados_cadastro.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(dados)

        st.success("Informações salvas com sucesso!")

with open("dados_cadastro.txt", "r", encoding='utf-8') as file:
    conteudo = file.read()

st.download_button(
    label="📥 Baixar dados cadastrados",
    data=conteudo,
    file_name="dados_cadastro.txt",
    mime="text/plain"
)
