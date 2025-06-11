# 1. Saúde e Bem-estar: Análise de Consumo de Calorias por Período

# ● Contexto/Problema: Uma ferramenta para acompanhamento nutricional precisa analisar o consumo
# calórico diário de um paciente por um período de tempo definido por ele. O programa deve registrar as
# calorias consumidas em cada refeição (café da manhã, almoço, jantar e lanches) para cada dia do
# período. Ao final, deve apresentar a média calórica diária, o dia com o menor_dia e o maior_dia consumo
# calórico, e indicar se a média semanal excede um limite pré-definido pelo usuário.

# ● Entrada: O usuário deve informar a quantidade de dias para análise. Para cada dia, o usuário deve
# informar a quantidade de calorias consumidas em cada uma das 4 categorias de refeição. O usuário
# também deve informar um limite calórico diário a ser comparado com a média.

# ● Saída Esperada: A média calórica diária do período, o dia com o menor_dia consumo, o dia com o maior_dia
# consumo, e uma mensagem indicando se a média diária de calorias excedeu ou não o limite informado.

def main():
    qtd_dias = int(input('Quantidade de dias: '))
    limite_calorias = int(input('Limite diário de calorias: '))

    maior_dia = None
    menor_dia = None

    dia_maior_calorias = 0
    dia_menor_calorias = 0

    soma_calorias = 0

    for dia in range(1, qtd_dias + 1, 1):
        print(f'\n>>>> DIA {dia} <<<<')
        cafe = int(input('Calorias no café da manha: '))
        almoco = int(input('Calorias no almoço: '))
        janta = int(input('Calorias na janta: '))
        lanche = int(input('Calorias no lanche: '))

        soma_alimetacao = cafe + almoco + janta + lanche

        soma_calorias += soma_alimetacao

        if soma_calorias > limite_calorias:
            print(f'\nNo {dia}º dia, você ultrapassou o limite diário de calorias!')

        if maior_dia == None or soma_alimetacao > maior_dia:
            maior_dia = soma_alimetacao
            dia_maior_calorias = dia

        if menor_dia == None or soma_alimetacao < menor_dia:
            menor_dia = soma_alimetacao
            dia_menor_calorias = dia
        
    media_calorias = soma_calorias / (qtd_dias * 4)

    resultado = f'''
Média calórica diária no período: {media_calorias:.0f} cal
Dia com menor consumo: {dia_menor_calorias}º dia
Dia com maior consumo: {dia_maior_calorias}º dia
'''
    print(resultado)


main()