# 8. Financeiro: Balanço de Fluxo de Caixa Mensal Detalhado

# ● Contexto/Problema: Para um controle financeiro mais rigoroso, é necessário registrar todas as
# receitas e despesas de um mês. O programa deve permitir que o usuário insira múltiplas receitas e
# múltiplas despesas. Para cada transação (seja receita ou despesa), o usuário deve informar uma
# descrição e o valor. Ao final, o programa deve apresentar o total de receitas, o total de despesas, o
# saldo final do mês e categorizar a despesa de maior valor e a receita de maior valor.

# ● Entrada: O usuário deve informar a quantidade de receitas a serem cadastradas e, para cada uma, a
# descrição e o valor. Em seguida, o usuário deve informar a quantidade de despesas a serem
# cadastradas e, para cada uma, a descrição e o valor.

# ● Saída Esperada: O total de receitas, o total de despesas, o saldo final do mês. A descrição e o valor da
# maior receita e da maior despesa.


def main():
    qtd_receitas = int(input('Quantidade de receitas: '))
    qtd_despesas = int(input('Quantidade de despesas: '))

    soma_receitas = 0
    soma_despesas = 0
    maior_receita = None
    maior_despesa = None

    print('\n-> RECEITAS <-')
    for receita in range(1, qtd_receitas + 1, 1):
        print(f'\n{receita}ª receita')
        receita = float(input(f'Valor: R$ '))
        soma_receitas += receita

        if maior_receita == None or receita > maior_receita:
            maior_receita = receita

    print(f'\nSoma das receitas: R$ {soma_receitas:.2f}')
    print('Finalizado o cadastro de receitas!')

    print('\n\n-> DESPESAS <-')
    for despesa in range(1, qtd_despesas + 1, 1):
        print(f'\n{despesa}ª despesa')
        despesa = float(input(f'Valor: R$ '))
        soma_despesas += despesa

        if maior_despesa == None or despesa > maior_despesa:
            maior_despesa = despesa
            
    print(f'\nSoma das despesas: R$ {soma_despesas:.2f}')
    print('Finalizado o cadastro de despesas!')

    saldo_final = soma_receitas - soma_despesas

    print(f'\nSaldo final do mês: R${saldo_final:.2f}\n')
    print(f'Maior receita: R${maior_receita:.2f}\nMaior despesa: R${maior_despesa:.2f}')


main()