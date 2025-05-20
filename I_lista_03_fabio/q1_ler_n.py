import utils

def main():
    contador = 1

    validar_contagem(contador)


def definir_contagem(n: int, contador: int):
    while contador <= n:
        print(contador)
        contador += 1


def validar_contagem(contador: int):
    n = utils.get_integer_number_min('Valor de N: ', 1)
    utils.linhas()

    print('>>> CONTAGEM <<<')
    definir_contagem(n, contador)

    
main()