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
def send_request(resquest_type, system_prompt, essay=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Payload para transcrição com imagem
    if resquest_type == "transcription" and essay:
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpg;base64,{essay}"
                            }
                        }
                    ]
                }
            ]
        }
   
    elif resquest_type == "grammar" or resquest_type == "cohesion" and essay:
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": essay
                }
            ]
        }

    # Payload padrão caso apenas o prompt de texto seja fornecido
    else:
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                }
            ]
        }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    return response
