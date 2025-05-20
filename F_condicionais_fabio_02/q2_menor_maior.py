from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    n1 = obter_numero_inteiro('Primeiro Número: ')
    n2 = obter_numero_inteiro('Segundo Número: ')

    linhas()
    
    maior_menor(n1, n2)


def maior_menor(n1: int, n2: int):
   if n1 > n1:
        print(f'Maior: {n1}\nMenor: {n2}')
   else:
        print(f'Maior: {n2}\nMenor: {n1}')


main()