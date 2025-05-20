import utils

def main():
    n = utils.get_integer_number_min('Quantidade de termos: ', 1)
    utils.linhas()

    print(f'>>> SEQUÊNCIA DE {n} TERMOS <<<')
    definir_sequencia(n)
    utils.linhas()


def definir_sequencia(n: int):
    contador = 1
    sequencia = 0

    while contador <= n:
        sequencia += contador
        print(sequencia)
        contador += 1


main()