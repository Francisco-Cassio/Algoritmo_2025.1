import os

def get_integer_number(label: str):
    try:
        num = int(input(label))
        return num
    except ValueError:
        linhas()
        print('O valor deve ser um número inteiro!\nTente novamente...')
        linhas()
        return get_integer_number(label)
    

def get_integer_number_min(label: str, min_value: int):
    num = get_integer_number(label)

    while num < min_value:
        linhas()
        print(f'O valor deve ser no mínimo {min_value}!\nTente novamente...')
        linhas()
        num = get_integer_number(label)

    return num
    

def get_decimal_number(label: str):
    try:
        num = float(input(label))
        return num
    except ValueError:
        linhas()
        print('O valor deve ser um valor numérico!\nTente novamente...')
        linhas()
        return get_decimal_number(label)
    

def linhas():
    print('-' * 30)
    

def limpar_tela():
    os.system('cls')