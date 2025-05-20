import utils

def main():
    contador = 1

    mostrar_pares(contador)
    

def calcular_par(n: int, contador: int):
    while contador <= n:
        if contador % 2 == 0:
            print(contador)
        contador += 1


def mostrar_pares(contador: int):
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()

    print('>>> CONTAGEM DOS PARES <<<')
    calcular_par(n, contador)


main()