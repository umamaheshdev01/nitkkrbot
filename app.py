import streamlit as st
import time

st.title('NIT Kurukestra Bot')
st.markdown('---')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

for chat in st.session_state['chat_history']:
    role = '🤖' if chat['role'] == 'model' else chat['role']
    with st.chat_message(role):
        st.write(chat['parts'])

prompt = st.chat_input("How can I help you!")

if prompt:
    st.session_state['chat_history'].append({'role': 'user', 'parts': prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner('Analyzing..'):
        time.sleep(2)

    bot_reply = 'Bot answered'
    st.session_state['chat_history'].append({'role': 'model', 'parts': bot_reply})

    with st.chat_message("🤖"):
        st.write(bot_reply)
