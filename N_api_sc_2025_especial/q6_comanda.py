# 6. (q6_comanda.py) Escreva um programa com menu para calcular
# o valor da comanda de pedidos de uma mesa em um bar.
# Operações:
# a. Inserir produtos: Cerveja (9 reais), Tira-Gosto (39 reais) e
# Água (5 reais). Entrada: “1 C” significa uma cerveja na
# conta. “3 A” 3 águas.
# b. Calcular a conta, incluindo 10% de taxa de serviço.
# c. Compras acima de 10 cervejas ou valor total superior a 200
# reais ficam isentos dos 10%
# d. Imprimir Conta: Pede quantas pessoas irão pagar.
# i. Valor da Conta e valor por pessoa.
# ii. Valor da taxa de serviço
# iii. Valor Total com taxa de serviço.
# e. Confirmar pagamento: que zera a conta da mesa.

# 25-05/8h43 - 25-05/15h39

import os
from q1_number_utils import obter_numero_inteiro_min


def main():
    conta = 0
    nota = ''

    cerveja = 9
    tira_gosto = 39
    agua = 5

    limpar_tela()
    definir_opcao(conta, nota, cerveja, tira_gosto, agua)


def definir_opcao(conta: int, nota: str, cerveja: float, tira_gosto: float, agua: float):
    print('''>>>> CÁSSIO'S BAR <<<<
-----------------------------------
1 - Inserir produtos
2 - Calcular nota
3 - Confirmar pagamento
4 - Sair
-----------------------------------''')
    
    escolha = int(input('Digite sua escolha: '))

    while True:
        limpar_tela()
        if escolha == 1:
            print('''-----------------------------------
Inserir Produtos:
    C - Cerveja
    T - Tira-gosto
    A - Água
            
OBS: Digite a quantidade e a inicial do que deseja.
    Ex: 3 A = 3 águas, 1 C = 1 cerveja
-----------------------------------''')

            entrada = input('Digite sua escolha: ')

            if entrada == '':
                limpar_tela()
                return definir_opcao(conta, nota, cerveja, tira_gosto, agua)
            
            escolha_a = int(entrada.split()[0])
            escolha_b = (entrada.split()[1]).upper()

            if escolha_b not in ('C', 'T', 'A'):
                limpar_tela()
                return definir_opcao(conta, nota, cerveja, tira_gosto, agua)

            if escolha_b == 'C':
                cerveja *= escolha_a
                conta += cerveja
                nota += f'''{escolha_a} Cerveja\t\tR$ {cerveja:.2f}
'''
            elif escolha_b == 'T':
                tira_gosto *= escolha_a
                conta += tira_gosto
                nota += f'''{escolha_a} Tira-Gosto\t\tR$ {tira_gosto:.2f}
'''
            elif escolha_b == 'A':
                agua *= escolha_a
                conta += agua
                nota += f'''{escolha_a} Água\t\t\tR$ {agua:.2f}
'''

            if conta <= 200:
                conta = conta + (conta * 0.1)
            
            input('Aperter <Enter> para continuar...')
            limpar_tela()
            return definir_opcao(conta, nota, cerveja, tira_gosto, agua)

        elif escolha == 2:
            qtd_pessoas = obter_numero_inteiro_min('Quantas pessoas irão pagar? ', 1)
            qtd_por_pessoa = conta / qtd_pessoas

            print(f'''
>>>> CÁSSIO'S BAR <<<<
-----------------------------------
{nota}-----------------------------------
Total a pagar:\t\tR${conta:.2f}
Valor por pessoa:\tR${qtd_por_pessoa:.2f}
-----------------------------------''')
            input('Aperter <Enter> para continuar...')
            limpar_tela()
            return definir_opcao(conta, nota, cerveja, tira_gosto, agua)

        elif escolha == 3:
            print('''Confirmado o pagamento!
-----------------------------------''')
            conta = 0
            nota = ''
            input('Aperter <Enter> para continuar...')
            limpar_tela()
            return definir_opcao(conta, nota, cerveja, tira_gosto, agua)
        
        elif escolha == 4:
            print('Saindo...')
            break


def limpar_tela():
    os.system('cls')


main()