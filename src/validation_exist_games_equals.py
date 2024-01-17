import json

def carregar_jogos_do_arquivo(response_api):
    with open("jogos.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)

    validar_dezenas_iguais(dados, response_api)

def validar_dezenas_iguais(dados, response_api):
    AMARELO = '\033[93m'
    RESET = '\033[0m'
    AZUL = '\033[94m'

    numerosJogosIguais = 0

    dezenas_today = response_api["listaDezenas"]

    for jogo in dados["jogos"]:
        dezenas = jogo["dezenas"]

        if jogo["data_apuracao"] == response_api["dataApuracao"]:
            return False

        if dezenas == dezenas_today:

            mensagem = f"\nja existe um jogo como esse no concurso {jogo['concurso']}"

            print(f"{AMARELO}{dezenas}{RESET}")
            print(f"{AMARELO}{dezenas_today}{RESET}")
            print(f"{AMARELO}{mensagem}{RESET}")
            numerosJogosIguais += 1

    mensagem = f"\nNo total temos {numerosJogosIguais} jogos repetidos nos ultimos Concursos da Lotofacil"

    print(f"{AZUL}{mensagem}{RESET}")