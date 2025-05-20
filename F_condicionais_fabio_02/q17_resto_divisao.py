from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num1 = obter_numero_inteiro('Primeiro Valor: ')
    num2 = obter_numero_inteiro('Segundo Valor: ')

    linhas()

    possibilidades(num1, num2)


def resto_divisao(n1: int, n2: int):
    return n1 % n2


def possibilidades(n1: int, n2: int):
    resto = resto_divisao(n1, n2)
    if resto == 1:
        print(f'{n1} + {n2} + {resto} = {n1 + n2 + resto}')
    elif resto == 2:
        if n1 % 2 == 0 and n2 % 2 == 0:
            print(f'{n1} e {n2} são pares')
        else:
            print(f'{n1} e {n2} são ímpares')
    elif resto == 3:    
        print(f'{n1 + n2} + {n1} = {n1 + n2 + n1}')
    elif resto == 4:
        if n2 != 0:
            print(f'{n1 + n2} / {n2} = {(n1 + n2) / n2}')
    else:
        print(f'{n1}² = {n1 ** 2}\n{n2}² = {n2 ** 2}')


main()