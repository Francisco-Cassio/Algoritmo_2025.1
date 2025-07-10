def main():
    obter_dia_inicio = input().split()
    dia_inicio = int(obter_dia_inicio[1])

    tempo_inicio = input().split(":")
    hora_inicio = int(tempo_inicio[0].strip())
    minuto_inicio = int(tempo_inicio[1].strip())
    segundo_inicio = int(tempo_inicio[2].strip())

    obter_dia_fim = input().split()
    dia_fim = int(obter_dia_fim[1])

    tempo_fim = input().split(":")
    hora_fim = int(tempo_fim[0].strip())
    minuto_fim = int(tempo_fim[1].strip())
    segundo_fim = int(tempo_fim[2].strip())

    total_segundos_inicio = segundo_inicio + (minuto_inicio * 60) + (hora_inicio * 3600) +  (dia_inicio * 86400)

    total_segundos_fim = segundo_fim + (minuto_fim * 60) + (hora_fim * 3600) + (dia_fim * 86400)

    segundos_totais = total_segundos_fim - total_segundos_inicio

    duracao_dias = segundos_totais // 86400
    segundos_restantes = segundos_totais % 86400

    duracao_horas = segundos_restantes // 3600
    segundos_restantes %= 3600

    duracao_minutos = segundos_restantes // 60
    duracao_segundos = segundos_restantes % 60

    print(f"{duracao_dias} dia(s)")
    print(f"{duracao_horas} hora(s)")
    print(f"{duracao_minutos} minuto(s)")
    print(f"{duracao_segundos} segundo(s)")

main()