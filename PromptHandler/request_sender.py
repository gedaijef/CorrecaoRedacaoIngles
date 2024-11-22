"""
Objetivo: Realizar request para OpenAI API
Data de Atualização: 25/10/2024
"""

# importações
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

# função para mandar o prompt lido para a api da OpenAi e pegar o retorno
def send_request(resquest_type, user_prompt, base64_image=None,text_file_path=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Payload para transcrição com imagem
    if resquest_type == "transcription" and base64_image:
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        }
   
    elif text_file_path:
        # Lendo o conteúdo do arquivo de texto
        with open(text_file_path, "r", encoding="utf-8") as file:
            text_content = file.read()

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
                        },
                        {
                            "type": "text_file",
                            "text_file_content": text_content
                        }
                    ]
                }
            ]
        }

        # Payload padrão caso apenas o prompt de texto seja fornecido
    else:
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
                        }
                    ]
                }
            ]
        }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    return response
