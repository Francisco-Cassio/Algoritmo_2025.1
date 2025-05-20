import utils

def main():
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()

    print('>>> VALOR DE S <<<')
    resultado = calcular_s(n)
    print(f"S para N = {n} é: {resultado}")
    utils.linhas()


def calcular_s(n: int):
    s = 0
    for i in range(n):
        if i % 2 == 0:
            numerador = i + 1
            denominador = n - i
        else:
            numerador = n - i
            denominador = i + 1
        
        termo = numerador / denominador
        if i % 2 == 1:
            termo *= -1
        
        s += termo
    return s


main()
