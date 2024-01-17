import certifi
import requests
import json

def consultar_endpoint(url):
    try:
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        dadosApiLotofacil = response.json()

        dataApuracao = dadosApiLotofacil["dataApuracao"]
        listaDezenas = dadosApiLotofacil["listaDezenas"]
        concurso = dadosApiLotofacil["numero"]

        adicionar_jogo(dataApuracao, listaDezenas, concurso)

        return dadosApiLotofacil

    except requests.exceptions.RequestException as e:
        print(f"\nErro ao consultar a endpoint: {e}")

def adicionar_jogo(data_apuracao, lista_dezenas, concurso):

    try:
        with open("jogos.json", "r") as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        dados = {"jogos": []}

    if not validation_exist_jogo_date_apuration(dados, concurso):
        novo_jogo = {"concurso": concurso, "data_apuracao": data_apuracao, "dezenas": lista_dezenas}
        dados["jogos"].insert(0, novo_jogo)

        with open("jogos.json", "w") as arquivo_json:
            json.dump(dados, arquivo_json, indent=2)

        VERDE = '\033[92m'
        RESET = '\033[0m'
        mensagem = "\nJogo adicionado com sucesso!"
        print(f"{VERDE}{mensagem}{RESET}")
    else:
        VERMELHO = '\033[91m'
        RESET = '\033[0m'
        mensagem = f"\nConcurso '{concurso}' ja esta salvo na nossa base de Jogos !"
        print(f"{VERMELHO}{mensagem}{RESET}")

def validation_exist_jogo_date_apuration(dados_jogos, concurso):

    for jogo in dados_jogos.get("jogos", []):
        if jogo["concurso"] == concurso:
            return True

    return False