import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM

# AGENTES PARA ESTUDO.
st.header("Agentes para Estudo")
st.write("Informe o tema e gere material para estudar:")

tema = st.text_input("Tema de estudo: ", placeholder="Ex.: Algoritmos")
objetivo = st.text_input("Objetivo: ", placeholder="Ex.: Entender conceitos")

executar = st.button("Gerar material")
api_key = 'SUA_API_KEY_AQUI'  # Substitua pela sua chave de API real

if executar:
    llm = LLM(
        model="groq/llama-3.3-70b-versatite",
        api_key=api_key,
        temperature=0.3
       # Tempereture: define o nivel de criatividade 
       # <= 0.3 mais deterministico
       # entre 0.4 e 0.7 equilibrado para explicações
       # maior que 0.7 mais criativo e menos previsível.
    )
        


