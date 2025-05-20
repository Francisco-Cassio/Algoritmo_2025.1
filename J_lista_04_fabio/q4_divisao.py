# 4. Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
# resultado da última divisão efetuada.

import utils

def main():
    num = utils.get_decimal_number('Digite um valor: ')
    utils.linhas()
    
    while num >= 1:
        num /= 2

    print(f'A última divisão teve como resultado: {num:.2f}')


main()