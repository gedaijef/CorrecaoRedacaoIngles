"""
Objetivo: Ler e retornar o conteúdo dos prompts
Data de Atualização: 25/10/2024
"""

# importção
from pathlib import Path
 

# função read_prompt - Faz a leitura do prompt 
def read_prompt(file):
    prompt_path = f"./Prompts/{file}.txt"
    path = Path(prompt_path)

    try:
        with open(path, "r", encoding="utf-8") as file:
            prompt_content = file.read()

        return prompt_content
    except FileNotFoundError:
        return None