import utils
from math import sqrt

def main():
    n = utils.get_integer_number_min('Digite um valor: ', 1)
    utils.linhas()

    verificar_quadrado(n)


def verificar_quadrado(n: int):
    contador = 1
    maior = 0

    while (contador ** 2) <= n:
        quadrado = contador ** 2
        if quadrado > maior:
            maior = quadrado
        contador += 1

    print(f'>>> O maior quadrado menor que {n} é:\n>>> {quadrado} (quadrado de {sqrt(quadrado)})')
    utils.linhas()


main()