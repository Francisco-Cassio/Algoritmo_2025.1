import utils

def main():
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()

    print('>>> VALOR DE S <<<')
    calcular_s(n)
    utils.linhas()


def calcular_s(n):
    soma = 0
    numerador = 1

    for denominador in range(1, n):
        soma += numerador / denominador
        numerador += 2

    print(f'>>>> S = {soma:.2f} <<<<')


main()