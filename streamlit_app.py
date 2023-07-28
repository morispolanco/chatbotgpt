import streamlit as st
import requests
import os

# Obtén la clave de API desde la variable de entorno
API_KEY = os.getenv('OPENAI_API_KEY')

def chat_with_gpt3(query, conversation_id):
    url = 'https://api.openai.com/v1/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'model': 'text-davinci-003',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': query, 'user': conversation_id}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Verificar si hubo errores en la solicitud
        response_data = response.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content']
        else:
            return 'No se obtuvo respuesta del modelo.'
    except requests.exceptions.RequestException as e:
        return f'Error en la solicitud: {e}'
    except KeyError as e:
        return f'Error al procesar la respuesta: {e}'

def main():
    st.title('Chat con GPT-3.5')
    conversation_id = st.text_input('Ingrese su ID de conversación', 'user123')
    user_query = st.text_input('Tú:', 'Hola')
    response = chat_with_gpt3(user_query, conversation_id)
    st.text_area('GPT-3.5:', response)

if __name__ == '__main__':
    main()
