# 5. Clima e Tempo: Monitoramento de Variações de Temperatura e Umidade

# ● Contexto/Problema: Um sistema de monitoramento climático registra a temperatura e a umidade a
# cada hora em um determinado local. O programa deve permitir que o usuário informe o número de
# horas para as quais os dados serão inseridos. Para cada hora, o usuário deve inserir a temperatura
# (°C) e a umidade (%). O programa deve identificar o maior pico de temperatura, o menor valor de
# umidade e a quantidade de vezes que a temperatura ultrapassou um limite predefinido pelo usuário.

# ● Entrada: O usuário deve informar a quantidade de horas para as quais os dados serão inseridos. Para
# cada hora, o usuário deve informar a temperatura e a umidade. O usuário também deve informar um
# limite de temperatura a ser monitorado.

# ● Saída Esperada: A maior temperatura registrada, a menor umidade registrada, e a contagem de vezes
# que a temperatura excedeu o limite predefinido.


def main():
    qtd_horas = int(input('Quantidade de horas: '))
    limite_temp = float(input('Limite de temperatura: '))

    maior_temp = None
    menor_umid = None
    contador = 0

    for hora in range(1, qtd_horas + 1, 1):
        print(f'\n{hora}ª HORA')
        temperatura = float(input(f'Temperatura atual: '))
        umidade = float(input(f'Umidade atual: '))

        if temperatura > limite_temp:
            print('\nA temperatura atual ultrapassou o limite')
            contador += 1

        if maior_temp == None or temperatura > maior_temp:
            maior_temp = temperatura

        if menor_umid == None or umidade < menor_umid:
            menor_umid = umidade

    res = f'''
Maior temperatura: {maior_temp:.1f} °C
Menor umidade: {menor_umid:.1f} %
O limite de temperatura foi ultrapassado {contador} vezes
'''

    print(res)


main()