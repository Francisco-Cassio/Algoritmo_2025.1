from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    dia1 = obter_numero_inteiro('Dia 01: ')
    mes1 = obter_numero_inteiro('Mês 01: ')
    ano1 = obter_numero_inteiro('Ano 01: ')
    linhas()
    dia2 = obter_numero_inteiro('Dia 02: ')
    mes2 = obter_numero_inteiro('Mês 02: ')
    ano2 = obter_numero_inteiro('Ano 02: ')

    linhas()

    if validar_ano(ano1, ano2):
        if validar_mes(mes1, mes2):
            if validar_data(dia1, mes1, ano1) and validar_data(dia2, mes2, ano2):
                    if ano1 < ano2:
                        print(f'Primeira Data: {dia1}/{mes1}/{ano1}\nSegunda Data: {dia2}/{mes2}/{ano2} <- MAIS RECENTE')
                    elif ano1 > ano2:
                        print(f'Primeira Data: {dia1}/{mes1}/{ano1} <- MAIS RECENTE\nSegunda Data: {dia2}/{mes2}/{ano2}')
                    else:
                        if mes1 < mes2:
                            print(f'Primeira Data: {dia1}/{mes1}/{ano1}\nSegunda Data: {dia2}/{mes2}/{ano2} <- MAIS RECENTE')
                        elif mes1 > mes2:
                            print(f'Primeira Data: {dia1}/{mes1}/{ano1} <- MAIS RECENTE\nSegunda Data: {dia2}/{mes2}/{ano2}')
                        else:
                            if dia1 < dia2:
                                print(f'Primeira Data: {dia1}/{mes1}/{ano1}\nSegunda Data: {dia2}/{mes2}/{ano2} <- MAIS RECENTE')
                            elif dia1 > dia2:
                                print(f'Primeira Data: {dia1}/{mes1}/{ano1} <- MAIS RECENTE\nSegunda Data: {dia2}/{mes2}/{ano2}')
                            else:
                                print(f'>>>> AS DATAS SÃO IGUAIS <<<<\nPrimeira Data: {dia1}/{mes1}/{ano1}\nSegunda Data: {dia2}/{mes2}/{ano2}')
            elif not validar_data(dia1, mes1, ano1) and validar_data(dia2, mes2, ano2):
                print(f'Data Inválida: {dia1}/{mes1}/{ano1}')
            elif validar_data(dia1, mes1, ano1) and not validar_data(dia2, mes2, ano2):
                print(f'Data Inválida: {dia2}/{mes2}/{ano2}')
            else:
                print(f'Data Inválida: {dia1}/{mes1}/{ano1}\nData Inválida: {dia2}/{mes2}/{ano2}')
                
        else:
            print('Mês não está correto!')
    else:
        print('Ano não está correto!')


def ano_bissexto(ano: int):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


def validar_mes(mes1: int, mes2: int):
    return 1 <= mes1 <= 12 and 1 <= mes2 <= 12


def validar_ano(ano1: int, ano2: int):
    return ano1 >= 1 and ano2 >= 1


def validar_data(dia: int, mes: int, ano: int):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= dia <= 31
    elif mes in (4, 6, 9, 11):
        return 1 <= dia <= 30
    else:
        if ano_bissexto(ano):
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
        

main()