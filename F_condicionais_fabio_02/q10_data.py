from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    dia = obter_numero_inteiro('Dia: ')
    mes = obter_numero_inteiro('Mês: ')
    ano = obter_numero_inteiro('Ano: ')

    linhas()

    if validar_ano(ano) and validar_mes(mes) and validar_data(dia, mes, ano):
        print(f'Esta data - {dia}/{mes}/{ano} - é VÁLIDA')
    else:
        print(f'Esta data - {dia}/{mes}/{ano} - é INVÁLIDA')


def ano_bissexto(ano: int):
    return ano % 4 == 0 and ano % 100 != 0 or  ano % 400 == 0
        

def validar_ano(ano: int):
    return ano >= 1


def validar_mes(mes: int):
    return 1 <= mes <= 12


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
    

main()
