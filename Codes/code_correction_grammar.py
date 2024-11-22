'''
Objetivo: Este código tem como objetivo corrigir a gramática dos textos transcritos das imagens.
Data de Atualização: 31/10/2024
'''

# Importações
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PromptHandler.request_sender import send_request
from PromptHandler.prompt_reader import read_prompt

# Função para corrigir a gramática do texto transcrito
def grammar_correction(file):
     # Verifica se o arquivo de transcrição existe
    if not os.path.exists(file):
        print("Erro: O arquivo de transcrição não foi encontrado.")
        return
    
    # Abra o arquivo no modo de leitura ('r')
    with open(file, "r") as arquivo:
    # Leia todo o conteúdo do arquivo e armazene na variável 'conteudo'
        conteudo = arquivo.read()

# Agora 'conteudo' é uma string com o texto do arquivo
    print(conteudo)
    user_prompt = read_prompt("grammar")

    response = send_request("grammar", user_prompt, conteudo)
    if response.status_code == 200:
        corrected_text = response.json()['choices'][0]['message']['content']

        # Define o caminho correto para salvar o arquivo corrigido
        output_dir = os.path.join('Text')
        output_path = os.path.join(output_dir, 'grammar_correction.txt')

        # Garante que o diretório de saída exista
        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(corrected_text)

        print("Correção gramatical salva com sucesso.")

    else:
        print(f"Erro na solicitação da API: {response.status_code}, {response.text}")

if __name__ == "__main__":
    file_name = r'Text\transcription.txt'
    grammar_correction(file_name)
