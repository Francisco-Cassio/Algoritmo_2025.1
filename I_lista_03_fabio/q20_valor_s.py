import utils

def main():
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()

    print('>>> VALOR DE S <<<')
    calcular_s(n)
    utils.linhas()


def calcular_s(n):
    s = 0
    for contador in range(1, n + 1):
        termo = 1 / contador
        if (contador + 1) % 2 == 0:
            termo *= -1
        s += termo

    print(f'>>>> S = {s:.2f} <<<<')


main()