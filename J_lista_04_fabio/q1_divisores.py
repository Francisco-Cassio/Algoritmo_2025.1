# 1. Leia uma lista de números e que para cada número lido, escreva o próprio número e a relação de seus
# divisores. (flag número = 0).

import utils

def main():
    num = utils.get_integer_number_min('Valor: ', 0)
    utils.linhas()

    print('>>> DIVISORES <<<\n')
    verificar_divisores(num)
    utils.linhas()


def verificar_divisores(n: int):

    while n != 0:
        contador = 1
        while contador <= n:
            
            if n % contador == 0:
                print(f'=> {contador} é divisor de {n}')
                
            contador += 1

        utils.linhas()
        n = utils.get_integer_number_min('Valor: ', 0)
        return verificar_divisores(n)



    
main()