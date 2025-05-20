from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num = obter_numero_inteiro('Valor de 4 dígitos: ')

    linhas()

    if soma_das_dezenas(num) == raiz_quadrada(num):
        print(f'Raiz Quadrada: {raiz_quadrada(num):.1f}')
        linhas()
        print(f'O número {num} é um quadrado perfeito')
    else:
        print(f'Raiz Quadrada: {raiz_quadrada(num):.1f}')
        linhas()
        print(f'O número {num} não é um quadrado perfeito')

def raiz_quadrada(num: int):
    return num ** (1/2)


def soma_das_dezenas(num: int):
    dezena1 = num // 100
    dezena2 = num % 100
    soma = dezena1 + dezena2
    print(f'Soma das dezenas: {dezena1} + {dezena2} = {soma}')
    return soma

main()