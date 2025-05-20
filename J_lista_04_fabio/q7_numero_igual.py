# 7. Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.

import utils

def main():
    num_a = utils.get_decimal_number('1º valor: ')
    utils.linhas()

    contador = 2
    while True:
        num_b = utils.get_decimal_number(f'{contador}° valor: ')
        utils.linhas()

        if num_b == num_a:
            break
        
        contador += 1

        
main()