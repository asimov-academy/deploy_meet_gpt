import streamlit as st

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# OPENAI UTILS =====================
client = openai.OpenAI()

def transcreve_audio(caminho_audio, language='pt', response_format='text'):
    with open(caminho_audio, 'rb') as arquivo_audio:
        transcricao = client.audio.transcriptions.create(
            model='whisper-1',
            language=language,
            response_format=response_format,
            file=arquivo_audio,
        )
    return transcricao

def chat_openai(
        mensagem,
        modelo='gpt-3.5-turbo-1106',
    ):
    mensagens = [{'role': 'user', 'content': mensagem}]
    reposta = client.chat.completions.create(
        model=modelo,
        messages=mensagens,
        )
    return resposta.choices[0].message.content

# TAB GRAVA REUNIÃO =====================
def tab_grava_reuniao():
    st.markdown('tab_gravar')

# TAB SELEÇÃO REUNIÃO =====================
def tab_selecao_reuniao():
    st.markdown('tab_selecao_reuniao')

# MAIN =====================
def main():
    st.header('Bem-vindo ao MeetGPT 🎙️', divider=True)
    tab_gravar, tab_selecao = st.tabs(['Gravar Reunião', 'Ver transcrições salvas'])
    with tab_gravar:
        tab_grava_reuniao()
    with tab_selecao:
        tab_selecao_reuniao()

if __name__ == '__main__':
    main()