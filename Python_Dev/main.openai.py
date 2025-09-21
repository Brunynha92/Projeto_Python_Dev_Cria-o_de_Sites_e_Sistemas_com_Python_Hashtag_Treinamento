# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

import streamlit as st
from openai import OpenAI

st.write("### ChatBot com IA") #markdow

modelo = OpenAI(api_key= "insira sua chave")

#session_state

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

# st.session_state["lista mensagem"].append(mensagem_do_usuario)

# Exibir historico de mensagens

for mensagem in st.session_state["lista_mensagem"]:
    print(mensagem)
    role = mensagem['role']
    texto = mensagem['content']
    st.chat_message(role).write(texto)

mensagem_do_usuario = st.chat_input("Escreva sua mensagem")

if mensagem_do_usuario:
    
    # user --> sr humando 
    # assistant --> IA 
    st.chat_message("user").write(mensagem_do_usuario)
    mensagem = {"role": "user", "content": mensagem_do_usuario}
    st.session_state["lista_mensagem"].append(mensagem)

    #resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages= st.session_state["lista_mensagem"],
        model= "gpt-4o"
    )


    resposta_ia = resposta_modelo.choices[0].message.content
    #exibir resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)


    # print(st.session_state["lista_mensagem"])

    
