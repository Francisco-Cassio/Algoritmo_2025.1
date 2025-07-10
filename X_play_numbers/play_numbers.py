import utils as u
import vetor_utils as v

def main():
    u.limpar_tela()
    vetor = []

    u.inicio()
    v.iniciar_playnumber(vetor)

    u.inicio_realizado()
    u.enter_to_continue()

    u.limpar_tela()

    while True:
        u.menu_principal()
        opcao = u.pedir_numero_faixa('\nOpção >>> ', 1, 16)
        print()

        if opcao == 1:
            v.mostrar_valores(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 2:
            v.resetar_vetor(vetor)
            print()
            print('Vetor resetado!')
            u.enter_to_continue()

        elif opcao == 3:
            qtd = v.ver_quantidade_itens(vetor)
            print(f'Quantidade de itens no vetor: {qtd}')
            print()
            u.enter_to_continue()

        elif opcao == 4:
            v. menor_maior_valor_posicao(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 5:
            somatorio = v.somatorio_valores(vetor)
            print(f'Somatório dos valores: {somatorio}')
            print()
            u.enter_to_continue()

        elif opcao == 6:
            media = v.media_valores(vetor)
            print(f'Média dos valores: {media:.2f}')
            print()
            u.enter_to_continue()

        elif opcao == 7:
            v.mostrar_positivos_quantidade(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 8:
            v.mostrar_negativos_quantidade(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 9:
            u.limpar_tela()

            u.regras()
            regra = u.pedir_numero_faixa('\nOpção >>> ', 1, 6)
            print()

            if regra == 1:
                valor = u.pedir_numero('Valor para multiplicar: ')
                vetor = v.mapear(vetor, lambda item:item * valor)

                print()
                print('Vetor atualizado!\n')
                u.enter_to_continue()

            elif regra == 2:
                valor = u.pedir_numero('Valor exponencial: ')
                vetor = v.mapear(vetor, lambda item:item ** valor)

                print()
                print('Vetor atualizado!\n')
                u.enter_to_continue()

            elif regra == 3:
                numerador, denominador = map(int, input('Fração (Ex: x/y): ').split('/'))

                vetor = v.mapear(vetor, lambda item:item * (numerador/denominador))

                print()
                print('Vetor atualizado!\n')
                u.enter_to_continue()
            
            elif regra == 4:
                minimo = u.pedir_numero('Faixa mínimo: ')
                maximo = u.pedir_numero('Faixa máximo: ')

                vetor = v.substituir_negativos(vetor, minimo, maximo)

                print()
                print('Vetor atualizado!\n')
                u.enter_to_continue()

            elif regra == 5:
                u.limpar_tela()
                u.ordenacao()

                ordem = u.pedir_numero('\nOpção >>> ')
                print()

                if ordem == 1:
                    vetor.sort()
                elif ordem == 2:
                    vetor.sort(reverse=True)

                print('Vetor atualizado!\n')
                u.enter_to_continue()


            elif regra == 6:
                vetor = v.embaralhar(vetor)
                print('Vetor atualizado!\n')
                u.enter_to_continue()

        elif opcao == 10:
            vetor = v.adicionar_valores(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 11:
            vetor = v.remover_valor_exato(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 12:
            vetor = v.remover_por_posicao(vetor)
            print()
            u.enter_to_continue()

        elif opcao == 13:
            vetor = v.editar_valor_posicao(vetor)
            print()
            u.enter_to_continue()
        
        elif opcao == 14:
            vetor = v.salvar_em_arquivo(vetor)
            print('Operação realizada com sucesso!!!')
            print()
            u.enter_to_continue()

        elif opcao == 15:
            arquivo = open('database.txt', 'a')
            arquivo.write(f'{vetor}\n')
            arquivo.close()
            u.limpar_tela()
            print('Salvo com sucesso!!!')
            break



main()