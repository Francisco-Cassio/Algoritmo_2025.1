# 9. Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
# prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
# quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
# clube (“a” ou “b”) e determinar os pontos obtidos por cada clube, de acordo com o seguinte critério:

# Lugar      Pontos
# 1           9
# 2           6
# 3           4
# 4           3

# Ao final, o algoritmo deve escreva os totais de pontos de cada clube, indicando o clube vencedor.

import utils

def main():
    n_prova = utils.get_integer_number_min('Número da prova: ', 0)
    qtd_nadadores = utils.get_integer_number_min('Quantidade de nadadores: ', 0)
    utils.linhas()

    pontos_a = 0
    pontos_b = 0

    while not (n_prova == 0 and qtd_nadadores == 0):
        atletas_lidos = 0

        while atletas_lidos < qtd_nadadores:
            nome = input('Nome: ')
            classificacao = utils.get_integer_number_min('Classificação: ', 1)
            tempo = utils.get_decimal_number('Tempo (seg): ')
            clube = input('Clube (a ou b): ').strip().lower()
            utils.linhas()

            if clube == 'a':
                pontos_a += validar_pontos(classificacao)
            elif clube == 'b':
                pontos_b += validar_pontos(classificacao)
            else:
                print('Clube inválido; nenhum ponto atribuído.')

            atletas_lidos += 1

        n_prova = utils.get_integer_number_min('Número da prova: ', 0)
        qtd_nadadores = utils.get_integer_number_min('Quantidade de nadadores: ', 0)
        utils.linhas()

    print(f'''>>>>> PLACAR DA COMPETIÇÃO <<<<<
-----------------------------------
=> PONTOS:
Clube A: {pontos_a}
Clube B: {pontos_b}
-----------------------------------''')

    if pontos_a > pontos_b:
        print('=> Clube A foi o vencedor')
    elif pontos_b > pontos_a:
        print('=> Clube B foi o vencedor')
    else:
        print('=> Empate')


def validar_pontos(classificacao: int) -> int:
    if classificacao == 1:
        return 9
    elif classificacao == 2:
        return 6
    elif classificacao == 3:
        return 4
    elif classificacao == 4:
        return 3
    else:
        return 0



main()