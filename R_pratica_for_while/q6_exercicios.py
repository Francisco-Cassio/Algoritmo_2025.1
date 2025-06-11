# 6. Saúde e Bem-estar: Análise de Progresso de Exercícios

# ● Contexto/Problema: Um treinador pessoal precisa monitorar o progresso de seus clientes em um
# determinado exercício ao longo de várias sessões. Para cada sessão de treino, o programa deve
# registrar o número de repetições realizadas e o peso levantado. O programa deve ser capaz de calcular
# o volume total (peso * repetições) para cada sessão e, ao final, identificar a sessão com o maior volume
# e a tendência de melhora (se o volume médio da segunda metade das sessões é maior que o da
# primeira metade).

# ● Entrada: O usuário deve informar a quantidade de sessões de treino para análise. Para cada sessão, o
# usuário deve informar o número de repetições e o peso levantado.

# ● Saída Esperada: Para cada sessão, o volume total. Ao final, indicar a sessão (pelo seu número ou
# identificador) com o maior volume e uma mensagem sobre a tendência de melhora (por exemplo,
# "Tendência de melhora observada" ou "Não houve melhora significativa").


def main():
    qtd_sessoes = int(input('Quantidade de sessões: '))

    maior_volume = None
    maior_sessao = None

    soma_primeira_metade = 0
    soma_segunda_metade = 0

    metade = qtd_sessoes // 2

    for sessao in range(1, qtd_sessoes + 1, 1):
        print(f'\nSessão {sessao}')
        peso = float(input("Peso (kg): "))
        repeticoes = int(input('Número de repetições: '))

        volume_total = peso * repeticoes

        print(f'\nVolume total: {volume_total:.1f}')

        if maior_volume == None or volume_total > maior_volume:
            maior_volume = volume_total
            maior_sessao = sessao

        if sessao <= metade:
            soma_primeira_metade += volume_total
        else:
            soma_segunda_metade += volume_total

    media_primeira = soma_primeira_metade / metade if metade > 0 else 0
    media_segunda = soma_segunda_metade / (qtd_sessoes - metade) if (qtd_sessoes - metade) > 0 else 0

    if media_primeira > media_segunda:
        print('\nNão há tendência de melhora')
    else:
        print('\nTendência de melhora observada')

    print(f'Sessão com maior volume: {maior_sessao}ª sessão')


main()
