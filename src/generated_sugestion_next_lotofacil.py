def generated_sugestion_next_lotofacil(contagem_numeros):
    RESET = '\033[0m'
    AZUL = '\033[94m'

    print("\n-----------------------------------------")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO"
    print(f"{AZUL}{mensagem}{RESET}")

    top_numeros = contagem_numeros.most_common(15)
    top_numeros = sorted(top_numeros, key=lambda x: x[0])


    print("Os 15 números que mais saíram:")
    for numero, repeticoes in top_numeros:
        print(f"Número {numero}: {repeticoes} vezes")