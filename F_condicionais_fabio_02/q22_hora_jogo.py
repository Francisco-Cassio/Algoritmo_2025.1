from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    hora_comeco = obter_numero_inteiro('Digite a hora de inicio do jogo: ')
    minutos_comeco = obter_numero_inteiro('Digite os minutos de inicio do jogo: ')
    linhas()
    hora_fim = obter_numero_inteiro('Digite a hora de fim do jogo: ')
    minutos_fim = obter_numero_inteiro('Digite os minutos de fim do jogo: ')

    linhas()

    calcular_hora(hora_comeco, minutos_comeco, hora_fim, minutos_fim)


def validar_hora(hora: int):
    return 0 <= hora <= 23


def validar_minutos(min: int):
    return 0 <= min <= 59


def calcular_hora(hora_c: int, min_c: int, hora_f: int, min_f: int):
    if validar_hora(hora_c) and validar_hora(hora_f):
        if validar_minutos(min_c) and validar_minutos(min_f):
            duracao_h = hora_f - hora_c
            duracao_m = min_f - min_c
            if hora_f < hora_c:
                duracao_h = (24 - hora_c) + hora_f
                if min_f < min_c:
                    duracao_m = (60 - min_c) + min_f
                    print(f'Duração: {duracao_h}h e {duracao_m} min')
                else:
                    print(f'Duração: {duracao_h}h e {duracao_m} min')
            else:
                print(f'Duração: {duracao_h}h e {duracao_m} min')


main()