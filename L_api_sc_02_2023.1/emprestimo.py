# João precisa de um dinheiro emprestado para comprar um Notebook para estudar programação. Para isso, foi ao RSBank fazer uma simulação. As taxas de empréstimo do banco obedecem à regra dos Juros Compostos Mensais, ou seja, o valor é calculado cumulativamente mês a mês, ou seja, aplica-se os juros sobre o valor total no primeiro mês e esse passa a ser a base para o segundo mês.
# Porém a taxa de juros aplicada é calculada de acordo com o prazo de parcelamento (vide tabela) e à SELIC, atualmente em 13,75% (abril/2023). O usuário só pode parcelar o empréstimo em até 24x (min. 2 parcelas). Valor mínimo de empréstimo é de um salário mínimo. Valor máximo de parcela é 40% da Renda Mensal do Cliente.
# Antes de calcular os juros é necessário calcular o IOF (Imposto sobre Operações Financeiras) pago ao Governo Federal antes de aplicar os Juros. O IOF é calculado da seguinte forma: 0,38% sobre valor total (independente do prazo) + 0,0082% por cada dia do prazo do empréstimo. Considere todos os meses com 30 dias. Os juros são aplicados sobre o valor a ser recebido pelo Cliente + IOF

# Prazo - Taxa
# Até 6x - 50% da SELIC
# de 7x a 12x - 75% da SELIC
# de 12x a 18x - 100% da SELIC
# Acima de 18x - 130% da SELIC

# ● Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo desejados, valide os dados a serem recebidos.
# ● Calcule e escreva na tela:
# a. Valor Pedido
# b. Valor do IOF
# c. Valor dos Juros a pagar
# d. Valor Total a pagar (ex.: "R$ 5148,00")
# e. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
# f. Comprometimento da Renda Mensal (%)
# g. Se Empréstimo APROVADO ou NEGADO

import utils

def main():
    renda_mensal = utils.get_decimal_number_min('Renda Mensal: R$ ', 1)
    valor_emprestimo = utils.get_decimal_number_min('Valor do Empréstimo: R$ ', 1)
    prazo = utils.get_integer_number_min('Prazo (parcelas): ', 1)
    utils.linhas()

    valor_pedido = valor_emprestimo

    iof = valor_emprestimo * (0.38/100) + valor_emprestimo * (0.0082/100) * (prazo *  30)
    valor_com_iof = valor_emprestimo + iof

    selic_anual = 13.75/100
    selic_mensal = selic_anual / 12

    emprestimo_com_juros = 0
    contador = 1

    if prazo <= 6:
        taxa_juros = 0.5 * selic_mensal
    elif prazo <= 12:
        taxa_juros = 0.75 * selic_mensal
    elif prazo <= 18:
        taxa_juros = 1 * selic_mensal
    else:
        taxa_juros = 1.3 * selic_mensal
        
    emprestimo_com_juros = valor_emprestimo * ((1 + taxa_juros) ** prazo)
    
    parcela = emprestimo_com_juros / prazo
    comprometimento = (parcela / renda_mensal) * 100
    juros = emprestimo_com_juros - valor_com_iof    

    if 2 <= prazo <= 24 and valor_emprestimo >= 1412 and parcela <= (renda_mensal * 0.4):
        situação = 'APROVADO'
    else:
        situação = 'NEGADO'

    print(f'''
Valor Pedido: R$ {valor_pedido:.2f}
Valor do IOF: R$ {iof:.2f}
Valor dos Juros: R$ {juros:.2f}
Valor Total a Pagar: R$ {emprestimo_com_juros:.2f}
Parcela Mensal: {prazo}x de R$ {parcela:.2f}
Comprometimento da Renda: {comprometimento:.2f}%
Empréstimo: {situação}''')

main()