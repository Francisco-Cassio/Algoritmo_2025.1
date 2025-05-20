from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    n1 = obter_numero_inteiro('Primeiro Número: ')
    n2 = obter_numero_inteiro('Segundo Número: ')
    n3 = obter_numero_inteiro('Terceiro Número: ')

    igual = eh_igual(n1, n2, n3)

    linhas()
    print(f'A quantidade de número iguais é: {igual}')


def eh_igual(n1: int, n2: int, n3: int):
    if n1 == n2 == n3:
        igual = 3
    elif n1 == n2 or n1 == n3 or n2 == n3:
        igual = 2
    else:
        igual = 0

    return igual


main()