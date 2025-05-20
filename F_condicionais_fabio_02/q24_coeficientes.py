from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    coeficiente_a = obter_numero_inteiro('Coeficiente A: ')
    coeficiente_b = obter_numero_inteiro('Coeficiente B: ')
    coeficiente_c = obter_numero_inteiro('Coeficiente C: ')

    linhas()

    x1 = calcular_raiz_um(coeficiente_a, coeficiente_b, coeficiente_c)
    x2 = calcular_raiz_dois(coeficiente_a, coeficiente_b, coeficiente_c)

    print(f'Equação: (-{coeficiente_b} ± √{coeficiente_b}² - 4 * {coeficiente_a} * {coeficiente_c}) / 2 * {coeficiente_a} ')
    linhas()
    print(f'Raiz 1: {x1:.1f}\nRaiz 2: {x2:.1f}')

def calcular_delta(a: int, b: int, c: int):
    if a != 0:
        return (b ** 2) + (4 * a * c)
    else:
        print('A deve ser diferente de 0')
        return


def calcular_raiz_um(a: int, b: int, c: int):
    return (-b + (calcular_delta(a, b, c) ** (1/2))) / 2 * a


def calcular_raiz_dois(a: int, b: int, c: int):
    return (-b - (calcular_delta(a, b, c) ** (1/2))) / 2 * a


main()