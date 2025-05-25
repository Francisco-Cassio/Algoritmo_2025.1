# 12. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
# responda quem ganha a partida. A partida chega ao final se:
# · Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
# · Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma
# diferença de 2 pontos sobre o adversário.

import utils
import os


def main():
    pontos_1 = 0
    pontos_2 = 0
    vencedor = ''

    while True:
        codigo = utils.get_integer_number_min_max('Código do jogador (1 ou 2): ', 1, 2)
        
        if codigo == 1:
            pontos_1 += 1
        elif codigo == 2:
            pontos_2 += 2


        if pontos_1 >= 21 and diferenca_pontos(pontos_1, pontos_2) >= 2:
            vencedor = 'Jogador 1'
            break
        elif pontos_2 >= 21 and diferenca_pontos(pontos_2, pontos_1) >= 2:
            vencedor = 'Jogador 2'
            break

    utils.limpar_tela()
    print(f'''>>>>> TORNEIO DE PING-PONG <<<<<
----------------------------------
Jogador 1: {pontos_1} pontos
Jogador 2: {pontos_2} pontos
----------------------------------
Vencedor: {vencedor}''')


def diferenca_pontos(p1: int, p2: int):
    return p1 - p2


main()