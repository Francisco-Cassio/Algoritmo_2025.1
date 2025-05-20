from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    n1 = obter_numero_inteiro('Primeiro Valor: ')
    n2 = obter_numero_inteiro('Segundo valor: ')
    linhas()
    operacao = obter_numero_inteiro(f'Qual operação deseja escolher?\n1 -> Adição\n2 -> Subtração\n3 -> Multiplicação\n4 -> Divisão\nDigite: ')

    adicao = calcular_adicao(n1, n2)
    subtracao = calcular_subtracao(n1, n2)
    multi = calcular_multiplicacao(n1, n2)
    divisao = calcular_divisao(n1, n2)

    linhas()

    if operacao == 1:
        print(f'{n1} + {n2} = {adicao}')
    elif operacao == 2:
        print(f'{n1} - {n2} = {subtracao}')
    elif operacao == 3:
        print(f'{n1} * {n2} = {multi}')
    else:
        print(f'{n1} / {n2} = {divisao}')



def calcular_adicao(n1: int, n2: int):
    return n1 + n2


def calcular_subtracao(n1: int, n2: int):
    return n1 - n2


def calcular_multiplicacao(n1: int, n2: int):
    return n1 * n2


def calcular_divisao(n1: int, n2: int):
    return n1 / n2


main()