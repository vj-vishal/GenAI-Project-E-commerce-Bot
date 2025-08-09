import streamlit as st
from router import router
from faq import ingest_faq_data,faq_chain
from pathlib import Path
from sql import sql_chain
from smalltalk import talk

fags_path= Path(__file__).parent/"resources/faq_data.csv"
ingest_faq_data(fags_path)

def ask(query):
    route= router(query).name
    if route=="faq":
        return faq_chain(query)
    elif route=="sql":
        return sql_chain(query)
    elif route=="smalltalk":
        return talk(query)
    else:
        return f"Route {route} not implemented"

st.title("E Commerce Chatbot")

query= st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"]= []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user","content":query})

    response= ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
