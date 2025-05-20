def calculo():
    quantia_solicitada = int(input("\nInforme a quantia em reais(R$) que você deseja organizar(obs: o valor tem que ser exato, sem centavos): "))
    notas_50 = quantia_solicitada // 50
    new_valor = quantia_solicitada - notas_50*50
    notas_10 = new_valor // 10
    ultimo_valor = new_valor - notas_10 * 10
    notas_1 = ultimo_valor // 1
    print(f'R${quantia_solicitada} precisa de: \n{notas_50} nota(s) de R$50 \n{notas_10} nota(s) de R$10 \n{notas_1} nota(s) de R$1')

calculo()