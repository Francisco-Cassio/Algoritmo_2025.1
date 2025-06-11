# 9. Imobiliário: Simulação de Pagamento de Financiamento Habitacional

# ● Contexto/Problema: Um comprador em potencial deseja simular o pagamento de um financiamento
# imobiliário. O programa deve solicitar o valor do imóvel, o valor da entrada, a taxa de juros mensal (fixa)
# e o número de parcelas. O programa deve calcular e exibir o valor de cada parcela (considerando juros
# compostos sobre o saldo devedor) e o saldo devedor restante após o pagamento de cada parcela.

# ● Entrada: O usuário deve informar o valor do imóvel, o valor da entrada, a taxa de juros mensal (em
# porcentagem) e o número total de parcelas.

# ● Saída Esperada: Para cada parcela, o número da parcela, o valor da parcela, o valor dos juros daquela
# parcela e o saldo devedor após o pagamento.


def main():
    valor_imovel = float(input('Valor do imóvel: R$ '))
    valor_entrada = float(input('Valor da entrada: R$ '))
    taxa_juros = float(input('Taxa (%): ')) / 100
    qtd_parcelas = int(input('Número de parcelas: '))

    saldo_devedor = valor_imovel - valor_entrada
    valor_parcela = (saldo_devedor * taxa_juros) / (1 - (1 + taxa_juros) ** (qtd_parcelas * (-1)))
    juros = 0
    amortizacao = 0

    for parcela in range(1, qtd_parcelas + 1, 1):
        print(f'\n{parcela}ª parcela:')
        juros = saldo_devedor * taxa_juros
        amortizacao = valor_parcela - juros
        saldo_devedor_atualizado = saldo_devedor - amortizacao
        saldo_devedor = saldo_devedor_atualizado

        res = f'''Valor da parcela: R$ {valor_parcela:.2f}
Valor do juros: R$ {juros:.2f}
Saldo devedor: R$ {saldo_devedor_atualizado:.2f}'''
        
        print(res)


main()


