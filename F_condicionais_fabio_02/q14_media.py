from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num1 = obter_numero_inteiro('Primeiro Valor: ')
    num2 = obter_numero_inteiro('Segundo Valor: ')
    num3 = obter_numero_inteiro('Terceiro Valor: ')
    num4 = obter_numero_inteiro('Quarto Valor: ')
    num5 = obter_numero_inteiro('Quinta Valor: ')

    linhas()

    media = calcular_media(num1, num2, num3, num4, num5)

    print(f'A média entre os valores é: {media:.1f}')
    linhas()
    maiores(num1, num2, num3, num4, num5)

def calcular_media(n1: int, n2: int, n3: int, n4: int, n5: int):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    return media


def maiores(n1: int, n2: int, n3: int, n4: int, n5: int):
    maior = calcular_media(n1, n2, n3, n4, n5)
    if n1 > maior:
        print(f'Valor maior que a média: {n1}')
    if n2 > maior:
        print(f'Valor maior que a média: {n2}')
    if n3 > maior:
        print(f'Valor maior que a média: {n3}')
    if n4 > maior:
        print(f'Valor maior que a média: {n4}')
    if n5 > maior:
        print(f'Valor maior que a média: {n5}')


main()