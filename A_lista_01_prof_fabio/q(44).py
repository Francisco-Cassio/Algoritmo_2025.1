def calculo():
    unidade_medida = input("\nInforme a unidade de medida: ")
    x1 = float(input("Infome a coordenada X do ponto 1 no plano: "))
    y1 = float(input("Informe a coordenada Y do ponto 1 no plano: "))

    x2 = float(input("Infome a coordenada X do ponto 2 no plano: "))
    y2 = float(input("Informe a coordenada Y do ponto 2 no plano: "))

    elemento = ((x2 - x1)**2 + (y2 - y1)**2)**1/2
    print(f'A distância entre o ponto1({x1:.1f}, {y1:.1f}) e o ponto2({x2:.1f}, {y2:.1f}) é de {elemento:.1f} {unidade_medida}')

calculo()

    