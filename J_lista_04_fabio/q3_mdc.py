# 3. Leia 2 (dois) números, calcule e escreva o mdc (máximo divisor comum) entre os números lidos.

import utils

def main():
    num1 = utils.get_intenger_number('Primeiro Valor: ')
    num2 = utils.get_intenger_number('Segundo Valor: ')
    utils.linhas()

    calcular_mdc(num1, num2)
    utils.linhas()

def calcular_mdc(num1, num2):
    maior = num1 if num1 > num2 else num2
    mdc = 0

    contador = 1

    while contador <= maior:
        if num1 % contador == 0 and num2 % contador == 0:
            mdc = contador
        
        contador += 1

    print(f'=> O MDC({num1}, {num2}) é: {mdc}')


main()