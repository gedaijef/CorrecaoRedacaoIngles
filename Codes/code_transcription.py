'''
Objetivo: Esse código tem como objetivo fazer a transcrição dos textos presentes nas fotos enviadas para a plataforma.
Data de Atualização: 31/10/2024
'''

# importações
import base64
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PromptHandler.request_sender import send_request
from PromptHandler.prompt_reader import read_prompt


# função convert_image - converte a imagem recebida em base64
def convert_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

# função transcribe_correction - Faz a transcrição do texto presente na imagem e salva um arquivo de texto com a transcrição
def transcribe_correction(image_path):
    # Validar tipo de arquivo
    if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Erro: O arquivo deve ser uma imagem do tipo PNG ou JPEG.")
        return

    system_prompt = read_prompt("transcription")
    base64_image = convert_image(image_path)  # Certifique-se de que a função de conversão esteja correta

    response = send_request("transcription", system_prompt, base64_image)

    if response.status_code == 200:
        returnGPT_transcription = response.json()['choices'][0]['message']['content']
        output_path = os.path.join("Text", "transcription.txt")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(returnGPT_transcription)

        print("Transcrição salva com sucesso.")
    else:
        print(f"Erro na solicitação da API: {response.status_code}, {response.text}")


if __name__ == "__main__":
  img = r'Images\Images\gabrielbreno_davinunes\img_1.jpeg'
  transcribe_correction(img)

  