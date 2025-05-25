import os

def get_integer_number(label: str):
    try:
       numero = int(input(label))
       return numero
    except ValueError:
        linhas()
        print('O valor deve ser um número inteiro!\nTente novamente...')
        linhas()
        return get_integer_number(label)
    

def get_integer_number_min(label: str, min_value: int):
    entrada = get_integer_number(label)

    while entrada < min_value:
        linhas()
        print(f'O valor deve ser no mínimo {min_value}!\nTente novamente...')
        linhas()
        entrada =  get_integer_number_min(label, min_value)

    return entrada


def get_integer_number_min_max(label: str, min_value: int, max_value: int):
    entrada = get_decimal_number(label)

    while entrada < min_value and entrada > max_value:
        linhas()
        print(f'O valor deve estar entre {min_value} e {max_value}!Tente novamente...')
        linhas()
        entrada = get_integer_number_min_max(label, min_value, max_value)

    return entrada


def get_decimal_number(label: str):
    try:
        num = float(input(label))
        return num
    except ValueError:
        linhas()
        print('O valor deve ser um valor numérico!\nTente novamente...')
        linhas()
        return get_decimal_number(label)


def get_decimal_number_min(label: int, min_value: int):
    entrada = get_decimal_number(label)

    while entrada < min_value:
        linhas()
        print(f'O valor deve ser no mínimo {min_value}!\nTente novamente...')
        linhas()
        entrada =  get_decimal_number_min(label, min_value)

    return entrada


def limpar_tela():
    os.system('cls')


def linhas():
    print('-' * 30)