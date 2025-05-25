# 4. (q4_mdc_rec.py) Implemente o Algoritmo MDC para determinar o
# Máximo Divisor Comum entre dois números inteiros positivos por
# meio de recursividade como estrutura de repetição.

# ínicio às 13h12 em 25/05

from q1_number_utils import obter_numero_inteiro_positivo


def main():
    num1 = obter_numero_inteiro_positivo('Primeiro valor: ')
    num2 = obter_numero_inteiro_positivo('Segundo valor: ')

    menor = num1 if num1 < num2 else num2
    mdc = 0
    contador = 1

    calcular_mdc(num1, num2, menor, contador, mdc)


def calcular_mdc(num1: int, num2: int, menor: int, contador: int, mdc: int):

    if num1 % contador == 0 and num2 % contador == 0:
        mdc = contador
        if mdc < menor:
            contador += 1
            if contador <= menor:
                return calcular_mdc(num1, num2, menor, contador, mdc)
    else:
        contador += 1
        if contador <= menor:
            return calcular_mdc(num1, num2, menor, contador, mdc)

    print(f'O MDC({num1}, {num2}) é: {mdc}')


main()

# Finalizado às 13h51 em 25/05