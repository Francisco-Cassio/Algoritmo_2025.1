import utils
import os

def main():
    utils.limpar_tela()
    qtd_eleitores = utils.get_integer_number_min('Quantidade de eleitores: ', 1)
    utils.linhas()
    utils.limpar_tela()

    sistema_eleitoral(qtd_eleitores)
    utils.linhas()


def sistema_eleitoral(n: int):
    votos1 = 0
    votos2 = 0
    votos3 = 0
    votos_nulos = 0
    votos_brancos = 0

    contador = 1

    while contador <= n:
        utils.limpar_tela()
        utils.linhas()
        print('>>> ELEICÃO NA BAIXA DA ÉGUA <<<')
        utils.linhas()
        print('\n>>> Escolha sua opção:\n>>> Lora - 1\n>>> Erick fi da Lora - 2\n>>> Rogério homi da Lora - 3\n>>> Voto Nulo - 9\n>>> Voto em Branco - 0\n')
        utils.linhas()
        print(f'ELEITOR N° {contador}:\n')
        voto = utils.get_integer_number_min('Voto: ', 0)
        utils.linhas()

        if voto == 1:
            votos1 += 1
        elif voto == 2:
            votos2 += 1
        elif voto == 3:
            votos3 += 1
        elif voto == 9:
            votos_nulos += 1
        elif voto == 0:
            votos_brancos += 1
        else:
            print('\nEscolha uma opção válida!\n')
            utils.linhas()
            print(f'ELEITOR N° {contador}:\n')
            voto = utils.get_integer_number_min('Voto: ', 0)
            utils.linhas()
    
        utils.limpar_tela()
        contador += 1

    definir_vencedor(n, votos1, votos2, votos3, votos_nulos, votos_brancos)


def definir_vencedor(n, votos1, votos2, votos3, votos_nulos, votos_brancos):
    print(f'>>> TOTAL DE VOTOS <<<\n')
    print(f'=> Rogério Silva: {votos1}\n=> Lora: {votos2}\n=> Franciéric: {votos3}\n\n=> Votos Nulos: {votos_nulos}\n=> Votos em Branco: {votos_brancos}')
    utils.linhas()

    if votos1 > votos2 and votos1 > votos3:
        print(f'\n>>> Lora é o(a) vencedor(a)!!!\n')
    elif votos2 > votos1 and votos2 > votos3:
        print(f'\n>>> Erick fi da Lora é o(a) vencedor(a)!!!\n')
    elif votos3 > votos1 and votos3 > votos2: 
        print(f'\n>>> Rogério homi da Lora é o(a) vencedor(a)!!!\n')
    else:
        if empate(votos1, votos2, votos3):
            input('\nCandidatos com as mesmas quantidades de votos!\nRefazendo a votação...\n(Aperte qualquer tecla) ')
            utils.linhas()
            utils.limpar_tela()
            sistema_eleitoral(n)


def empate(votos1: int, votos2: int, votos3: int):
    return votos1 == votos2 or votos1 == votos2 or votos2 == votos3


main()