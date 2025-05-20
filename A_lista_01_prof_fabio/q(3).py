min = int(input("Informe os minutos: "))

def conversao():
    horas = min//60
    min_resto = min%60
    tempo_formatado = print(f'{min}min são {horas}h e {min_resto}min')
    return tempo_formatado

conversao()