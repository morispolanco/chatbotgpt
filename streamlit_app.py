import streamlit as st
import requests
import os

# Obtén la clave de API desde la variable de entorno
API_KEY = os.getenv('OPENAI_API_KEY')

def chat_with_gpt3(query, conversation_id):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'model': 'text-davinci-002',  # GPT-3.5 model
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': query, 'user': conversation_id}]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

def main():
    st.title('Chat with GPT-3.5')
    conversation_id = st.text_input('Enter your conversation ID', 'user123')
    user_query = st.text_input('You:', 'Hello')
    response = chat_with_gpt3(user_query, conversation_id)
    st.text_area('GPT-3.5:', response)

if __name__ == '__main__':
    main()
