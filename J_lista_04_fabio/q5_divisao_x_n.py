# 5. Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada
# divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até
# chegar a 2.

import utils

def main():
    x = utils.get_decimal_number('Valor de X: ')
    n = utils.get_decimal_number('Valor de N: ')
    utils.linhas()

    while n > 2:
        divisao = x / n
        print(f'{divisao:.2f}')
        x = divisao
        n -= 1


main()