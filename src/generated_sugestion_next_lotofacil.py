import heapq
def generated_sugestion_next_lotofacil(contagem_numeros):
    RESET = '\033[0m'
    AZUL = '\033[94m'

    print("\n-----------------------------------------")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO - 15 DEZENAS"
    print(f"{AZUL}{mensagem}{RESET}")

    top_numeros = contagem_numeros.most_common(15)
    top_numeros = sorted(top_numeros, key=lambda x: x[0])


    print("Os 15 números que mais saíram:")
    for numero, repeticoes in top_numeros:
        print(f"Número {numero}: {repeticoes} vezes")


    print("\n-----------------------------------------")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO - 16 DEZENAS"
    print(f"{AZUL}{mensagem}{RESET}")

    top_numeros = contagem_numeros.most_common(16)
    top_numeros = sorted(top_numeros, key=lambda x: x[0])


    print("Os 16 números que mais saíram:")
    for numero, repeticoes in top_numeros:
        print(f"Número {numero}: {repeticoes} vezes")


    print("\n-----------------------------------------")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO - 17 DEZENAS"
    print(f"{AZUL}{mensagem}{RESET}")

    top_numeros = contagem_numeros.most_common(17)
    top_numeros = sorted(top_numeros, key=lambda x: x[0])

    print("Os 17 números que mais saíram:")
    for numero, repeticoes in top_numeros:
        print(f"Número {numero}: {repeticoes} vezes")

    print("\n-----------------------------------------")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO - 18 DEZENAS"
    print(f"{AZUL}{mensagem}{RESET}")

    top_numeros = contagem_numeros.most_common(18)
    top_numeros = sorted(top_numeros, key=lambda x: x[0])

    print("Os 18 números que menos saíram:")
    for numero, repeticoes in top_numeros:
        print(f"Número {numero}: {repeticoes} vezes")

    print("\n-----------------------------------------")
    print("NUMEROS QUE MENOS SAIRAM")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO - 15 DEZENAS"
    print(f"{AZUL}{mensagem}{RESET}")

    bottom_numeros = heapq.nsmallest(15, contagem_numeros.items(), key=lambda x: x[1])
    bottom_numeros = sorted(bottom_numeros, key=lambda x: x[0])

    print("Os 15 números que menos saíram:")
    for numero, repeticoes in bottom_numeros:
        print(f"Número {numero}: {repeticoes} vezes")

    print("\n-----------------------------------------")

    mensagem = "SUGESTAO DE PROXIMO CONCURSO - 18 DEZENAS"
    print(f"{AZUL}{mensagem}{RESET}")

    bottom_numeros = heapq.nsmallest(18, contagem_numeros.items(), key=lambda x: x[1])
    bottom_numeros = sorted(bottom_numeros, key=lambda x: x[0])

    print("Os 18 números que menos saíram:")
    for numero, repeticoes in bottom_numeros:
        print(f"Número {numero}: {repeticoes} vezes")