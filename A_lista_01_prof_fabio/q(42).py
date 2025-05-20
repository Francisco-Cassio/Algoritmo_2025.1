def calculo():
    custo_de_fabrica = float(input("Informe o custo de fábrica(R$): "))
    precentagem_distribuidor = custo_de_fabrica * 0.28
    impostos = custo_de_fabrica * 0.45
    custo_consumidor = custo_de_fabrica + precentagem_distribuidor + impostos
    print(f'O custo de final do consumidor será de R${custo_consumidor}')

calculo()