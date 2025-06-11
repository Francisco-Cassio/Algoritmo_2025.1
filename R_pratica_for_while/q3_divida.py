# 3. Financeiro: Projeção de Dívida com Pagamentos Variáveis

# ● Contexto/Problema: Um indivíduo possui uma dívida com juros compostos mensais e deseja projetar
# como ela se comportará ao longo do tempo, considerando pagamentos variáveis. O programa deve
# permitir que o usuário insira o valor inicial da dívida, a taxa de juros mensal e o número de meses para
# projeção. Para cada mês, o usuário deve informar o valor do pagamento realizado. O programa deve
# mostrar o saldo da dívida após cada pagamento e indicar em qual mês a dívida foi quitada (se for o
# caso), ou o saldo remanescente.

# ● Entrada: O usuário deve informar o valor inicial da dívida, a taxa de juros mensal (em porcentagem) e
# a quantidade de meses para a projeção. Para cada mês, o usuário deve informar o valor do pagamento
# realizado.

# ● Saída Esperada: O saldo da dívida ao final de cada mês. Uma mensagem indicando se a dívida foi
# quitada, em qual mês isso ocorreu, ou o saldo remanescente ao final da projeção.

def main():
    divida = float(input('Valor inicial da dívida: R$ '))
    taxa = int(input('Valor da taxa (%): ')) / 100
    meses = int(input('Quantidade de meses: '))

    juros = 0
    soma_pagamento = 0
    saldo_pre_pagamento = 0

    for mes in range(1, meses + 1, 1):
        print(f'\nMês {mes}')
        juros = divida * taxa
        saldo_pre_pagamento = divida + juros

        print(f'Saldo antes do pagamento: R${saldo_pre_pagamento:.2f}')
        pagamento = float(input('Valor do pagamento deste mês: '))
        soma_pagamento += pagamento

        divida = saldo_pre_pagamento - pagamento

        print(f'Saldo atual R${divida:.2f}')

        if divida <= 0:
            print(f'\nDívida quitada no {mes}º mês')
            break

    if divida > 0:
        print(f'\nSaldo remanescente: R${divida:.2f}')


main()
