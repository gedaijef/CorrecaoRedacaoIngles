'''
Objetivo: Este código tem como objetivo corrigir a coesão baseados na estrutura do texto transcrito.
Data de Atualização: 31/10/2024
'''

# Importações
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PromptHandler.request_sender import send_request
from PromptHandler.prompt_reader import read_prompt

# Função cohesion_correction - Faz a correção da coesão com base no gênero do texto
def cohesion_correction(file):
    # Verifica se o arquivo de transcrição existe
    transcribed_path = f"./Transcricao/Text/{file}"
    if not os.path.exists(transcribed_path):
        print("Erro: O arquivo de transcrição não foi encontrado.")
        return

    user_prompt = read_prompt("cohesion")

    response = send_request("cohesion", user_prompt, transcribed_path)

    if response.status_code == 200:
        corrected_text = response.json()['choices'][0]['message']['content']

        output_path = os.path.join("./Transcricao/Text", "cohesion_correction.txt")

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(corrected_text)

        print("Correção de coesão salva com sucesso.")

    else:
        print(f"Erro na solicitação da API: {response.status_code}, {response.text}")

if __name__ == "__main__":
    file_name = input("Digite o nome do arquivo de transcrição (ex: transcription.txt): ")
    cohesion_correction(file_name)
