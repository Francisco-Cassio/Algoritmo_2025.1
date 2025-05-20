from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num1 = obter_numero_inteiro('Primeiro Valor: ')
    num2 = obter_numero_inteiro('Segundo Valor: ')
    num3 = obter_numero_inteiro('Terceiro Valor: ')
    num4 = obter_numero_inteiro('Quarto Valor: ')
    num5 = obter_numero_inteiro('Quinto Valor: ')

    linhas()

    maior = eh_maior(num1, num2, num3, num4, num5)
    menor = eh_menor(num1, num2, num3, num4, num5)
    
    if sao_diferentes(num1, num2, num3, num4, num5):
        print(f'=> Menor Valor: {menor}\n=> Maior Valor: {maior}')
    else:
        print('Todos os valores devem ser diferentes!')


def sao_diferentes(n1: int, n2: int, n3: int, n4: int, n5: int):
    return n1 != n2 and n1 != n3 and n1 != n4 and n1 != n5 and n2 != n3 and n2 != n4 and n2 != n5 and n3 != n4 and n3 != n5 and n4 != n5


def eh_maior(n1: int, n2: int, n3: int, n4: int, n5: int):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    
    return maior


def eh_menor(n1: int, n2: int, n3: int, n4: int, n5: int):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    if n4 < menor:
        menor = n4
    if n5 < menor:
        menor = n5
    
    return menor


main()