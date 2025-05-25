# 5. (q5_primos.py) Escreva uma função que verifique todos os
# números de N até M, escreva ao lado de cada número se é ou
# não primo.

# Ínicio às 8h23 em 25/05

from q1_number_utils import obter_numero_inteiro_min


def main():
    n = obter_numero_inteiro_min('Limite N: ', 0)
    m = obter_numero_inteiro_min('Limite M: ', n + 1)
    
    while n <= m:
        if eh_primo(n):
            print(f'{n} é primo')
        else:
            print(f'{n} não é primo')
        
        n += 1


def eh_primo(n):
    contador = 2

    while contador <= (n - 1):
        while n % contador == 0:
            return False
        contador += 1
    return True


main()

# Finalizado às 8h42 em 25/05