import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
    Tu es un professeur de sciences au lycée. Sois clair, concis et pédagogue. 
    Explique les réponses en utilisant des exemples simples et un langage adapté aux élèves de 16 ans.

    Voici des informations tirées d'un document fourni par l'utilisateur :
    {doc_context}

    Voici l'historique de la conversation :
    {chat_context}

    Question : {question}

    Réponse :
"""

# Langchain Setup
model = OllamaLLM(model = "mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


st.set_page_config(page_title= "🏫Ali-Prof de Teccart",
                   layout="centered")
st.title("👨🏻‍🏫Ali-prof de Teccart")

