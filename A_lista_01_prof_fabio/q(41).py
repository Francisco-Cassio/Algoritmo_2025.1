def calculo():
    anos = int(input("Informe a quantos anos fuma: "))
    num_cigarros_dia = int(input("Informe o número de cigarros fumados por dia: "))
    preco_carteira = float(input("Informe o preço da carteira de cigarro(R$): "))
    preco_1_cigarro = preco_carteira/20

    dinheiro_gasto = anos*num_cigarros_dia*preco_1_cigarro
    print(f'O indiíviduo gastou ao longo de {anos} ano(s) R${dinheiro_gasto:.2f} com cigarros')

calculo()