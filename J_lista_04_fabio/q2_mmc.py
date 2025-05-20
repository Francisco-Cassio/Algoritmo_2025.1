# 2. Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.

import utils

def main():
    num1 = utils.get_intenger_number('Primeiro Valor: ')
    num2 = utils.get_intenger_number('Segundo Valor: ')
    utils.linhas()

    calcular_mmc(num1, num2)
    utils.linhas()


def calcular_mmc(n1: int, n2: int):
    maior = n1 if n1 > n2 else n2
    mmc = maior

    while not (mmc % n1 == 0 and mmc % n2 == 0):
        mmc += maior

    print(f'=> O MMC({n1}, {n2}) é: {mmc}')


main()