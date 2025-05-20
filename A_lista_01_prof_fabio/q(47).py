def calculo():
    quantidade_latao = float(input("\nInforme quantos Kg de latão você deseja: "))
    valor_cobre = quantidade_latao * 0.7
    valor_zinco = quantidade_latao * 0.3
    print(f'Para se obter {quantidade_latao}Kg de latão, será necessário {valor_cobre:.2f}Kg de cobre e {valor_zinco:.2f}Kg de zinco')

calculo()