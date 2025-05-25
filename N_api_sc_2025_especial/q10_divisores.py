# (q10_divisores.py) Receba dois valores inteiro A e B positivos com
# B > A em pelo menos 11 unidades. Em seguida, mostre todos os
# valores de A até B, e coloque ao lado a quantidade de divisores
# desse número. Exemplo:
# G (n)
# H (n)
# I (n)
# J (n)

# 25-05/14h48 - 25-05/15h07

from q1_number_utils import obter_numero_inteiro_min


def main():
    A = obter_numero_inteiro_min('Valor de A: ', 1)
    B = obter_numero_inteiro_min('Valor de B: ', A + 11)

    contador = 1
    qtd_divisores = 0

    while A < B:
        while contador <= A:
            if A % contador == 0:
                qtd_divisores += 1
            contador += 1
        print(f'{A} ({qtd_divisores})')
        contador = 1
        qtd_divisores = 0
        A += 1


main()