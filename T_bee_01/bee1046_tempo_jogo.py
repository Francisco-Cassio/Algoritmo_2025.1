def main():
    hora_inicio, hora_final = map(int, input().split())

    tempo_jogo = 0

    if hora_inicio < hora_final:
        tempo_jogo = hora_final - hora_inicio
    elif hora_final < hora_inicio:
        tempo_jogo = (24 - hora_inicio) + hora_final
    else:
        tempo_jogo = 24
    
    print(f'O JOGO DUROU {tempo_jogo} HORA(S)')


main()