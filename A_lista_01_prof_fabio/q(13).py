def calculo():
    valor = float(input("\nDigite uma quantia(R$): "))
    valor_70 = valor * 0.7
    print(f'70% de R${valor:.2f} são R${valor_70:.2f}')

calculo()