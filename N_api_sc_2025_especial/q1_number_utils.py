# 1. (q1_number_utils.py) Faça funções auxiliares para as seguintes
# situações abaixo, utilizando como estrutura de repetição
# Exclusivamente WHILE:
# a. Receber número inteiro
# b. Receber número inteiro positivo
# c. Receber número inteiro negativo
# d. Receber número inteiro de no mínimo X
# e. Receber número inteiro de no máximo X
# f. Receber número inteiro numa faixa min X e max Y

# 24-05/19h56 - 24-05/20h10

def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print('O valor deve ser um número inteiro!')
        return obter_numero_inteiro(label)
    

def obter_numero_inteiro_positivo(label: str):
    numero = obter_numero_inteiro(label)

    while numero < 0:
        print('O valor deve ser positivo!')
        return obter_numero_inteiro_positivo(label)

    return numero


def obter_numero_inteiro_negativo(label: str):
    numero = obter_numero_inteiro(label)

    while numero > 0:
        print('O valor deve ser negativo!')
        return obter_numero_inteiro_negativo(label)

    return numero


def obter_numero_inteiro_min(label: str, min_value: int):
    numero = obter_numero_inteiro(label)

    while numero < min_value:
        print(f'O valor deve ser no mínimo {min_value}')
        return obter_numero_inteiro_min(label, min_value)
    
    return numero


def obter_numero_inteiro_max(label: str, max_value: int):
    numero = obter_numero_inteiro(label)

    while numero < max_value:
        print(f'O valor deve ser no mínimo {max_value}')
        return obter_numero_inteiro_max(label, max_value)
    
    return numero


def obter_numero_inteiro_min_max(label: str, min_value: int, max_value: int):
    numero = obter_numero_inteiro(label)

    while numero < min_value or numero > max_value:
        print(f'O  valor deve estar no intervalo entre {min_value} e {max_value}!')
        return obter_numero_inteiro_min_max(label, min_value, max_value)
    
    return numero