# 3. (q3_covid.py) Durante a Pandemia da COVID, diariamente o
# noticiário informava à população dados importantes sobre a
# evolução e controle da doença. Neste cenário, usa-se atualmente
# o conceitos de “Em queda”, “Em Alta” e “Em Estabilidade”
# baseada nos números do dia. Variações menores que 15% nos
# números indicam "Em Estabilidade".
# Construa um programa que calcule e classifique a variação dos
# dados de acordo com o explicado. As entradas são vários
# números que representam a quantidade casos no dia. Os
# operadores podem, por erro, digitar valores inválidos com letras,
# números negativos, ou outros valores absurdos.
# Considerar apenas os inteiros não negativos. O programa deve
# parar quando for digitado exatamente “fim”. Após cada número
# mostrar o conceito do dia, ou “valor não computador” caso o valor
# seja inválido. E após o fim, mostrar total de casos, e média de
# casos por dia.

# Ínicio às 21h52 em 24/05

from q1_number_utils import obter_numero_inteiro_positivo


def main():
    medida = obter_numero_inteiro_positivo(f'Quantidade de casos: ')
    total_casos = 0
    total_dias = 0

    print('Em Estabilidade')
    calcular_casos(medida, total_casos, total_dias)


def calcular_casos(medida: int, total_casos: int, total_dias: int):
    while True:
        casos = input(f'Quantidade de casos: ')

        if casos.lower() == 'fim':
            break
        else:
            try :
                casos = int(casos)

                queda = medida - (medida * 0.15)
                alta = medida + (medida * 0.15)

                medida = casos

                if casos < 0:
                    print('valor não computado')
                    return calcular_casos(medida, total_casos, total_dias)
                
            except ValueError:
                print('valor não computado')
                return calcular_casos(medida, total_casos, total_dias)

        total_casos += casos
        total_dias += 1

        if casos >= alta:
            situacação = 'Em Alta'
        elif casos <= queda:
            situacação = 'Em Queda'
        else:
            situacação = 'Em Estabilidade'

        print(situacação)

    media = total_casos / total_dias

    print(f'''Total de casos: {total_casos}
Média de casos por dia: {media:.1f}''')


main()

# Finalizado às 23h23 em 24/05