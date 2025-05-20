import utils

def main():
    n_compras = utils.get_integer_number_min('Número de compras: ', 1)
    faturamento = 0
    total_cashback = 0

    cashback = 0

    maior = None
    menor = None

    while n_compras >= 1:
        utils.linhas()
        nome_cliente = input('Seu nome: ')
        valor_compras = utils.get_decimal_number_min('R$ ', 1)
        faturamento += valor_compras

        if valor_compras <= 250:
            cashback = valor_compras * 0.05
            total_cashback += cashback

        elif valor_compras <= 500:
            cashback = valor_compras * 0.07
            total_cashback += cashback

        elif valor_compras <= 750:
            cashback = valor_compras * 0.08
            total_cashback += cashback

        else:
            cashback = (((250 * 0.05) + (500 * 0.07)) + (750 * 0.08)) + valor_compras * 0.25
            total_cashback += cashback

        
        if maior is None or cashback > maior:
            maior = cashback

        if menor is None or cashback < menor:
            menor = cashback
        
        n_compras -= 1

    percentual_cashback = (total_cashback / faturamento) * 100
    media = (maior + menor) / 2

    resultado = f'''
>>>>> LOJA <<<<<
-----------------------------------
Faturamento: R$ {faturamento:.2f}
-----------------------------------
Cashback distribuído (valor em reais): R$ {total_cashback:.2f}
Percentual do cashback investido: {percentual_cashback:.2f}%
-----------------------------------
Maior valor em cashback: R$ {maior:.2f}
Valor Médio em cashback: R$ {media:.2f}
Menor valor em cashback: R$ {menor:.2f}
-----------------------------------
'''
    
    utils.limpar_tela()
    print(resultado)


main()