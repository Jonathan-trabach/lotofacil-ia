import json
from collections import Counter
import generated_sugestion_next_lotofacil

def contar_repeticoes_numeros(jogos):
    contagem_numeros = Counter()

    for jogo in jogos:
        dezenas = jogo["dezenas"]
        contagem_numeros.update(dezenas)

    return contagem_numeros


def validacao_repeticao_numeros():
    with open("jogos.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    jogos = dados["jogos"]

    contagem_numeros = contar_repeticoes_numeros(jogos)

    print("\n-----------------------------------------")
    print("Contagem de repetições de cada número:")

    for numero, repeticoes in sorted(contagem_numeros.items()):
        print(f"Número {numero}: {repeticoes} vezes")

    generated_sugestion_next_lotofacil.generated_sugestion_next_lotofacil(contagem_numeros)
