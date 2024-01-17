import src.get_and_save_lotofacil as get_and_save_lotofacil
import src.validation_exist_games_equals as validation_exist_games_equals
import src.validation_quantity_dezenas_equals as validation_quantity_dezenas_equals

def main():
    endpoint_url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil"
    response_api = get_and_save_lotofacil.consultar_endpoint(endpoint_url)

    validation_exist_games_equals.carregar_jogos_do_arquivo(response_api)

    validation_quantity_dezenas_equals.validacao_repeticao_numeros()

if __name__ == "__main__":
    main()
