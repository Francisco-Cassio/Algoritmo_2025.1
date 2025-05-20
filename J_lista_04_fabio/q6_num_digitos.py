# 6. Escreva um algoritmo para determinar o número de dígitos de um número informado.

import utils

def main():
    num = input('Digite um valor: ')
    utils.linhas()

    contador = 1

    while contador < len(num):
        contador += 1
    
    print(f'O número tem {contador} dígitos')


main()