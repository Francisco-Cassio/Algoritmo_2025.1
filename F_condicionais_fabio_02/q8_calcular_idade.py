from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    dia_nascimento = obter_numero_inteiro('Dia do Nascimento: ')
    mes_nascimento = obter_numero_inteiro('Mês do Nascimento: ')
    ano_nascimento = obter_numero_inteiro('Ano de Nascimento: ')
    linhas()
    dia_atual = obter_numero_inteiro('Dia Atual: ')
    mes_atual = obter_numero_inteiro('Mês Atual: ')
    ano_atual = obter_numero_inteiro('Ano Atual: ')

    linhas()

    if validar_ano(ano_atual, ano_nascimento) and validar_mes(mes_atual, mes_nascimento):

        idade = calcular_idade(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual)
        
        if not validar_data(dia_nascimento, mes_nascimento, ano_nascimento):
            print(f'Data de Nascimento Inválida: {dia_nascimento}/{mes_nascimento}/{ano_nascimento}')
            
        if not validar_data(dia_atual, mes_atual, ano_nascimento):
            print(f'Data Atual Inválida: {dia_atual}/{mes_atual}/{ano_atual}')
        
        if validar_data(dia_nascimento, mes_nascimento, ano_nascimento) and validar_data(dia_atual, mes_atual, ano_nascimento):
            print(f'Data Atual: {dia_atual}/{mes_atual}/{ano_atual}')
            print(f'Data de Nascimento: {dia_nascimento}/{mes_nascimento}/{ano_nascimento}')
            print(f'===> IDADE: {idade} <===')


def ano_bissexto(ano: int):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


def validar_ano(ano_a: int, ano_n: int):
    return ano_a >= 1 and ano_n >= 1


def validar_mes(mes_a: int, mes_n: int):
    return 1 <= mes_a <= 12 and 1 <= mes_n <= 12


def validar_data(dia: int, mes: int, ano: int):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= dia <= 31
    elif mes in (4, 6, 9, 11):
        return 1 <= dia <= 30
    elif mes == 2:
        if ano_bissexto(ano):
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28


def calcular_idade(dia_n: int, mes_n: int, ano_n: int, dia_a: int, mes_a: int, ano_a: int):
    idade = ano_a - ano_n
    if (mes_a, dia_a) < (mes_n, dia_n):
        idade -= 1
    return idade


main()