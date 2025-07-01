def main():
    hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

    inicio = hora_inicial * 60 + minuto_inicial
    fim = hora_final * 60 + minuto_final

    if fim <= inicio:
        fim += 24 * 60

    duracao = fim - inicio
    horas = duracao // 60
    minutos = duracao % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

    
main()