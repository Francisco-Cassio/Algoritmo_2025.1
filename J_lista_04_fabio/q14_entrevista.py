# 14. Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O
# entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então
# responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada
# entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
# · a porcentagem de cada candidato;
# · a porcentagem dos outros candidatos;
# · a porcentagem de eleitores indecisos;
# · a porcentagem de votos nulos/brancos;
# · o total de entrevistados;
# · uma mensagem indicando a possibilidade ou não de haver 2° turno.

import utils


def main():
    print('''>>>>> ENTREVISTA <<<<<
-----------------------------------
Serra:\t\t45
Dilma:\t\t13
Ciro Gomes:\t23
              
Indeciso:\t99
Nulo/Branco:\t0''')
    
    utils.linhas()

    votos_1 = 0
    votos_2 = 0
    votos_3 = 0
    votos_indecisos = 0
    votos_brancos_nulos = 0
    total_entrevistados = 0

    while True:
        candidato = utils.get_integer_number_min('Escolha seu candidato: ', -1)
        utils.linhas()

        if candidato == -1:
            break

        votos_1, votos_2, votos_3, votos_indecisos, votos_brancos_nulos = calcular_votos(candidato, votos_1, votos_2, votos_3, votos_indecisos, votos_brancos_nulos)

        total_entrevistados += 1
    
    pct_candidato1 = (votos_1 / total_entrevistados) * 100
    pct_candidato2 = (votos_2 / total_entrevistados) * 100
    pct_candidato3 = (votos_3 / total_entrevistados) * 100
    pct_indecisos = (votos_indecisos / total_entrevistados) * 100
    pct_brancos_nulos = (votos_brancos_nulos / total_entrevistados) * 100
    
    utils.linhas()
    print(f'''PORCENTAGEM:
    Serra (45):\t\t{pct_candidato1:.0f}%
    Dilma (13):\t\t{pct_candidato2:.0f}%
    Ciro Gomes (23):\t{pct_candidato3:.0f}%

    Indecisos:\t\t{pct_indecisos:.0f}%
    Brancos/Nulos:\t{pct_brancos_nulos:.0f}%
------------------------------------
Total de entrevistados:\t{total_entrevistados}
------------------------------------''')


def calcular_votos(candidato: int, votos_1: int, votos_2: int, votos_3: int, votos_indecisos: int, votos_brancos_nulos: int):
    if candidato == 45:
        votos_1 += 1
    elif candidato == 13:
        votos_2 += 1
    elif candidato == 23:
        votos_3 += 1
    elif candidato == 99:
        votos_indecisos += 1
    elif candidato == 0:
        votos_brancos_nulos += 1
    else:
        print('Escolha uma opção válida!')
        utils.linhas()
        candidato = utils.get_integer_number_min('Escolha seu candidato: ', -1)
        utils.linhas()
        return calcular_votos(candidato, votos_1, votos_2, votos_3, votos_indecisos, votos_brancos_nulos)

    return votos_1, votos_2, votos_3, votos_indecisos, votos_brancos_nulos

main()