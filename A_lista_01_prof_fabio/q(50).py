def calculo():
    valor_produto = float(input("\nInforme o preço do produto(R$): "))
    valor_parcela = valor_produto // 3
    valor_entrada = (valor_produto%3) + valor_parcela
    print(f'Parcelamento:\nEntrada: R${valor_entrada:.2f}\nParcelas: 2x de R${valor_parcela:.2f}')

calculo()