import utils
from random import randint

def main():
    tamanho = utils.get_integer_number_min('A senha terá quantos dígitos? ', 1)

    gerar_senha(tamanho)


def gerar_senha(n):
    ...


def diferenca(atual: str, anterior: str):
    diff = atual - anterior
    if diff > 1:
        return True
    elif diff < -1:
        diff *= -1
        return True
    else:
        return False


main()