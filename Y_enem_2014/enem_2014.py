import utils as u, vetor_utils as v

def main():
    arquivo = v.carregar_arquivo('enem2014_nota_por_escola.txt')

    menu = '''========== ENEM POR ESCOLA - 2014 ==========

1 - Top N Brasil (todas as áreas) 
2 - Top N Brasil por área
3 - Top N por estado
4 - Top N por estado e rede (pública ou privada)
5 - Média nacional por área
6 - Melhor escola por área e estado
7 - Lista de escolas por estado ordenada por renda
8 - Busca escola específica por parte do nome
9 - Ranking ENEM por estado
10 - Ranking ENEM por região do país

0 - Sair

============================================

>>> Opção: '''

    u.limpar_tela()
    opcao = u.obter_numero(menu)

    while opcao != 0:
        print()
        if opcao == 1:
            n = u.obter_numero_positivo('Informe o valor N de escolas: ')
            print()
            print('============================================\n')
            v.topn_brasil(arquivo, n)
            print('\n============================================')

        elif opcao == 2:
            n = u.obter_numero_positivo('Informe o valor N de escolas: ')
            print()
            areas = v.menu_areas()
            u.limpar_tela()
            area = u.obter_numero_positivo(areas)
            print()
            print('============================================\n')
            v.topn_brasil_area(arquivo, area, n)
            print('\n============================================')

        elif opcao == 3:
            u.limpar_tela()
            n = u.obter_numero_positivo('Informe o valor N de escolas: ')
            estado = input('Informe a sigla do estado (Ex: MA, PI): ').upper()
            print()
            print('============================================\n')
            v.topn_estado(arquivo, estado, n)
            print('\n============================================')

        elif opcao == 4:
            u.limpar_tela()
            n = u.obter_numero_positivo('Informe o valor N de escolas: ')
            estado = input('Informe a sigla do estado (Ex: MA, PI): ').upper()
            rede = input('Informe a rede (pública ou federal): ').title()
            print()
            print('============================================\n')
            v.top_estados_rede(arquivo, estado, rede, n)
            print('\n============================================')

        elif opcao == 5:
            areas = v.menu_areas()
            u.limpar_tela()
            area = u.obter_numero_positivo(areas)
            print()
            print('============================================\n')
            v.media_nacional_area(arquivo, area)
            print('\n============================================')
            
        elif opcao == 6:
            areas = v.menu_areas()
            u.limpar_tela()
            area = u.obter_numero_positivo(areas)
            u.limpar_tela()
            estado = input('Informe a sigla do estado (Ex: MA, PI): ').upper()
            print()
            print('============================================\n')
            v.melhor_escola_area_estado(arquivo, area, estado)
            print('\n============================================')

        elif opcao == 7:
            estado = input('Informe a sigla do estado (Ex: MA, PI): ').upper()
            u.limpar_tela()
            print('============================================\n')
            v.ordenar_estado_renda(arquivo, estado)
            print('\n============================================')

        elif opcao == 8:
            u.limpar_tela()
            parte_nome = input('Informe o nome da escola (inteiro ou partes): ').upper()
            print()
            print('============================================\n')
            v.procurar_nome(arquivo, parte_nome)
            print('\n============================================')

        elif opcao == 9:
            estado = input('Informe a sigla do estado (Ex: MA, PI): ').upper()
            u.limpar_tela()
            print('============================================\n')
            v.ranking_enem_estado(arquivo, estado)
            print('\n============================================')

        elif opcao == 10:
            u.limpar_tela()
            n = u.obter_numero_positivo('Informe o valor N de escolas: ')
            estado = input('Informe a sigla do estado (Ex: MA, PI): ').upper()
            print()
            print('============================================\n')
            v.ranking_enem_regiao(arquivo, estado, n)
            print('\n============================================')

        u.enter_continue()
        opcao = u.obter_numero(menu)

    u.limpar_tela()
    print('Saindo...')


main()