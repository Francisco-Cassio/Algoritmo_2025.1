import utils

def main():
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()

    print('>>> VALOR DE S <<<')
    calcular_s(n)
    utils.linhas()


def calcular_s(n: int):
    contador = 1
    s = 0

    while contador <= n:
        s += (1/contador)
        contador += 1

    print(f'>>>> S = {s:.2f} <<<<')


main()