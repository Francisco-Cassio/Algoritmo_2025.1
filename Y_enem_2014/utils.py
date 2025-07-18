import os

def obter_numero(label):
    entrada = input(label)
    try:
        num = int(entrada)
        return num
    except ValueError:
        print('O valor deve ser um número! Tente novamente...')
        return obter_numero(label)


def obter_numero_positivo(label):
    num = obter_numero(label)

    if num < 0:
        print('O valor deve ser um número positivo! Tente novamente...')
        return obter_numero_positivo(label)
    
    return num


def limpar_tela():
    os.system('cls')


def enter_continue():
    print()
    input('Aperte <Enter> para continuar...')
    limpar_tela()