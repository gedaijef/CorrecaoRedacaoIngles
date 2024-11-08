# Vai receber os parâmetros da dela e chamar os codes
# Importações necessárias
from Codes.code_transcription import transcribe_correction  # Certifique-se de importar corretamente
from Codes.code_correction_cohesion import cohesion_correction
from Codes.code_correction_grammar import grammar_correction

def main():
    # Exibir opções para o usuário
    tipo_redacao = input("Selecione o tipo de redação: ")
    arquivo_imagem = input("Anexe o arquivo da redação: ")
    
    # Chamada da função de transcrição
    transcribe_correction(arquivo_imagem)  # Aqui você pode modificar a função para aceitar o arquivo como argumento
    
    # Exibir opções de correção
    tipo_correcao = input("Selecione o tipo de correção (gramática/cohesão): ")

    # Aqui você pode chamar a função de correção com base no tipo de correção selecionado
    if tipo_correcao == "gramática":
        # Chame a função de correção gramatical
        feedback = grammar_correction()
    elif tipo_correcao == "cohesão":
        # Chame a função de correção de coesão
        feedback = cohesion_correction()

    # Exibir feedback ao usuário
    print(feedback)

if __name__ == "__main__":
    main()
