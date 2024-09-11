import streamlit as st
import time
from bot import chatbaby

st.title('NIT Kurukestra Bot')
st.markdown('---')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{"role": "model", "parts": "Great to meet you. What would you like to know?"}]

for chat in st.session_state['chat_history']:
    role = '🤖' if chat['role'] == 'model' else chat['role']
    with st.chat_message(role):
        st.write(chat['parts'])

prompt = st.chat_input("How can I help you!")

if prompt:
    try:
        st.session_state['chat_history'].append({'role': 'user', 'parts': prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("🤖"):
            message_placeholder = st.empty()
            message_placeholder.write("Loading...")

        bot_reply = chatbaby(st.session_state['chat_history'], prompt)
        st.session_state['chat_history'].append({'role': 'model', 'parts': bot_reply})

        message_placeholder.write(bot_reply)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.stop()
