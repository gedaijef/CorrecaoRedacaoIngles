# Recebe os parâmetros da tela e chamar os codes
from Codes.code_transcription import transcribe_correction
from Codes.code_correction_cohesion import cohesion_correction
from Codes.code_correction_grammar import grammar_correction

def main():    
    transcribe_correction('Images\essay.jpeg')
    
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
