import utils
import os

def main():
    pesquisa = '''
>>>> ESCOLHA UMA OPÇÃO <<<<
-----------------------------------
1 - Incluir Item
2 - Imprimir Lista
3 - Sair
-----------------------------------'''

    menu = '''
------- PESQUISA DE PREÇOS -------'''

    contador = 0
    preco_total = 0

    while True: 
        utils.limpar_tela()
        print(pesquisa)
        escolha = utils.get_decimal_number_min('Digite: ', 1)
        utils.limpar_tela()
        
        if escolha == 3:
            break

        elif escolha == 1:
            contador += 1
            
            utils.linhas()
            item = input('Nome do produto: ')
            peso = input('Peso do produto: ')
            preco = float(input('Preço do produto: R$ '))
            utils.linhas()
    
            preco_total += preco
            preco = str(preco).replace('.', ',')

            produto = f'''\n{contador} - {item.capitalize()} ({peso})\tR$ {preco}'''

            menu += produto

            utils.enter_continue()
            utils.limpar_tela()

        elif escolha == 2:
            preco_total = str(preco_total).replace('.', ',')

            print(menu)
            print('-----------------------------------')
            print(f'Valor total: R$ {preco_total}\n')
            utils.linhas()

            opcaoes = input('Deseja ver as opções de parcelas? (S/N): ')

            if opcaoes.upper() == 'S':
                utils.limpar_tela()
                preco_total = float(preco_total.replace(',', '.'))
                
                parcelar(preco_total)

            else:
                utils.linhas()
                utils.enter_continue()
                utils.limpar_tela()


def parcelar(preco_total: float):
        parcelamento = '''
----- OPÇÕES DE PARCELAMENTO -----
1. Parcelar em até 3x - A partir de R$ 30,00 em compras
2. Parcelar em até 5x - A partir de R$ 100,00 em compras
3. Parcelar em até 6x - Juros Compostos com taxa de 5% ao mês
'''
        print(parcelamento)
        print(f'Valor total: R$ {preco_total}')

        utils.linhas()
        opcao_parcela = utils.get_decimal_number_min('Escolha um opção de parcela: ', 1)
        utils.linhas()
        qtd_parcela = utils.get_decimal_number_min('Parcelar em quantas vezes? ', 1)
        utils.linhas()

        if opcao_parcela == 1:
            if 30 < preco_total <= 100:
                if qtd_parcela > 3:
                    input('Para este valor, só é possível parcelar em até 3x\nAperte <Enter> para tentar novamente...')
                    utils.limpar_tela()
                    return parcelar(preco_total)
                else:
                    parcelas = preco_total / qtd_parcela
                    print(f'Valor das parcelas: R$ {parcelas:.2f}')
            else:
                input('Apenas para valores a partir de R$ 30,00 e menores que R$ 100,00\nAperte <Enter> para tentar novamente...')
                utils.limpar_tela()
                return parcelar(preco_total)
            
        elif opcao_parcela == 2:
            if preco_total > 100:
                parcelas = preco_total / qtd_parcela
                print(f'Valor das parcelas: R$ {parcelas:.2f}')
            else:
                input('Apenas para valores a partir de R$ 100,00\nAperte <Enter> para tentar novamente...')
                utils.limpar_tela()
                return parcelar(preco_total)

        elif opcao_parcela == 3:
            parcelas = 0
            count = 1
            count_parcelas = qtd_parcela

            preco_total = preco_total / qtd_parcela

            while count_parcelas >= 1:
                parcelas = ((preco_total * 0.05) + preco_total)
                preco_total = parcelas
                print(f'{count}° Parcela: R$ {parcelas:.2f}')
                count_parcelas -= 1
                count += 1

        utils.linhas()

        utils.enter_continue()
        utils.limpar_tela()


main()