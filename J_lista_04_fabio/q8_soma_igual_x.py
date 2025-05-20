# 8. Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
# quando a soma de dois números consecutivos da lista for igual a X.

import utils

def main():
    num = utils.get_intenger_number('Digite um valor: ')
    utils.linhas()

    calcular_ciclo(num)


def calcular_ciclo(num: int):
    contador = 0
    soma = 0

    while soma < num:
        while contador < 2:
            n = utils.get_decimal_number('Valor: ')

            soma += n
            contador += 1
        
        utils.linhas()
        if soma > num or soma < num:
            return calcular_ciclo(num)


main()