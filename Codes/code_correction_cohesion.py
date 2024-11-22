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
    if not os.path.exists(file):
        print("Erro: O arquivo de transcrição não foi encontrado.")
        return
    
    with open(file, "r") as arquivo:
        essay = arquivo.read()
    
    essay = "##Redação: " + essay
    system_prompt = read_prompt("cohesion")
    response = send_request("cohesion", system_prompt, essay)

    if response.status_code == 200:
        corrected_text = response.json()['choices'][0]['message']['content']

        output_dir = os.path.join('Text')
        output_path = os.path.join(output_dir, 'cohesion_correction.txt')

        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(corrected_text)

        print("Correção de coesão salva com sucesso.")

    else:
        print(f"Erro na solicitação da API: {response.status_code}, {response.text}")

if __name__ == "__main__":
    file_name = r'Text\\transcription.txt'
    cohesion_correction(file_name)
