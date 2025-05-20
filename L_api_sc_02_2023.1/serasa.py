# A SERASA começou a implantar o Serasa Score 2.0 em 2021. O Score é uma forma de avaliar o perfil do consumidor no momento da
# aquisição de crédito, seja cartão de crédito ou financiamento de um veículo, apartamento ou empréstimo pessoal. Desta forma são avaliadas algumas
# entradas de dados históricos consumidor e, caso não esteja negativado, apresentando um valor entre 0 e 1000.
# Baseado nisso, faça um programa que receba valores de 0 a 100 em cada um dos 3 critérios de cálculo, ou seja, como se fosse uma Escala, no item
# a. você pode ter de 0 a 100, se for 100, por exemplo, significa 100% dos pontos previstos, assim Score 1.0 (260) e Score 2.0 (620), se fosse 50%
# então esse item a. seria 130 e 310, respectivamente em cada Score 1.0 e 2.0. Aplique essa formula de cada uma e apresente o valor do Score tanto
# versão Score 1.0 quanto na versão Score 2.0.

# Critérios de cálculo                Serasa Score 1.0    Serasa Score 2.0

# a. Dados positivos (cartão de
# crédito, consórcio, consignado,
# empréstimos e financiamentos)           26% (260)           62% (620)
# comportamentos de pagamento,
# tempo dos contratos e tipos de
# contratos                           


# b. Informações de dívidas, histórico    57% (570)           19% (190)
# de regularização e em aberto



# c. Consultas para novos contratos       17% (170)           19% (190)
# de serviço ou crédito


# Com os dois Scores (1.0 e 2.0) calculados, classifique o Perfil do
# Cliente acordo com a tabela abaixo e apresente a ele o resultados:

# Classificação de risco de tomador de crédito:

# Faixa de score      Score antigo        Score novo
# Muito bom           800-1000            701-1000
# Bom                 600-800             501-700
# Regular             400-600             301-500
# Baixo               0-400               0-300

# Exemplo entrada:
# a: 70
# b: 55
# c: 100
# Saída:
# Score 1.0: valor - categoria
# Score 2.0: valor - categoria

import utils

def main():
    nota_a = utils.get_integer_number_min('Nota de 0 a 100 para o critério A: ', 1)
    nota_b = utils.get_integer_number_min('Nota de 0 a 100 para o critério B: ', 1)
    nota_c = utils.get_integer_number_min('Nota de 0 a 100 para o critério C: ', 1)
    utils.linhas()

    score1_a = calculo_score(260, nota_a)
    score1_b = calculo_score(570, nota_b)
    score1_c = calculo_score(170, nota_c)

    score2_a = calculo_score(620, nota_c)
    score2_b = calculo_score(190, nota_c)
    score2_c = calculo_score(190, nota_c)

    nota_score1 = score1_a + score1_b + score1_c
    nota_score2 = score2_a + score2_b + score2_c

    classificacao01 = classificacao_score01(nota_score1)
    classificacao02 = classificacao_score02(nota_score2)

    print(f'Score 1.0: {nota_score1:.2f} - {classificacao01}')
    print(f'Score 2.0: {nota_score2:.2f} - {classificacao02}')


def classificacao_score01(nota_score1):
    if nota_score1 <= 400:
        return 'Baixo'
    elif nota_score1 <= 600:
        return 'Regular'
    elif nota_score1 <= 800:
        return 'Bom'
    else:
        return 'Muito Bom'

def classificacao_score02(nota_score2):
    if nota_score2 <= 300:
        return 'Baixo'
    elif nota_score2 <= 500:
        return 'Regular'
    elif nota_score2 <= 700:
        return 'Bom'
    else:
        return 'Muito Bom'


def calculo_score(valor, nota):
    return valor * (nota / 100)


main()