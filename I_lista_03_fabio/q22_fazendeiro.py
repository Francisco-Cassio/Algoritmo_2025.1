import utils

def main():
    n = utils.get_integer_number_min('Quantidade de fichas: ', 1)
    utils.linhas()

    print('>>> IDENTIFICAÇÃO <<<\n')
    definir_ficha(n)


def definir_ficha(n: int):
    contador = 1

    n_magro = 0
    n_gordo = 0
    peso_magro = 0
    peso_gordo = 0

    while contador <= n:
        n_identificacao = utils.get_integer_number_min('Número de Identificação: ', 1)
        nome = input('Nome: ')
        peso = utils.get_decimal_number('Peso (kg): ')
        utils.linhas()

        if peso > peso_gordo:
            peso_gordo = peso
            n_gordo = n_identificacao
        else:
            peso_magro = peso
            n_magro = n_identificacao
        
        contador += 1
        
    print(f'>>> BOI MAIS MAGRO:\n>>> N° Identificação: {n_magro}\n>>> Peso (kg): {peso_magro:.2f}\n')
    print(f'>>> BOI MAIS GORDO:\n>>> N° Identificação: {n_gordo}\n>>> Peso (kg): {peso_gordo:.2f}')
    utils.linhas()



main()