import utils

def main():
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()
    somatorio = 0
    contador = 1

    calcular_soma(n, somatorio, contador)


def calcular_soma(n: int, somatorio: int, contador: int):
    while contador <= n:
        somatorio += contador
        contador += 1

    if n > 0:
        print(f'A soma dos números entre 1 e {n} é {somatorio}')
        utils.linhas()
    else:
        print('O valor deve ser maior ou igual a 1')
        utils.linhas()
        n = utils.get_integer_number_min('Valor de N: ', 1)
        utils.linhas()
        return calcular_soma(somatorio, contador)


main()