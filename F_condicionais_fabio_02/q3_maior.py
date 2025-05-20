from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    n1 = obter_numero_inteiro('Primeiro Número: ')
    n2 = obter_numero_inteiro('Segundo Número: ')
    n3 = obter_numero_inteiro('Terceiro Número: ')

    maior = eh_maior(n1, n2, n3)
    
    linhas()
    print(f'Dentre os valores, o maior é {maior}')


def eh_maior(n1: int, n2: int, n3: int):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    return maior


main()