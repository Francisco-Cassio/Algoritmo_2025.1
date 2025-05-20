def calculo_area_retangulo():
    unidade_medida = input("Informe a unidade de medida: ")
    base = float(input(f'Informe o valor da base do retângulo({unidade_medida}): '))
    altura = float(input(f'Informe o valor da altura do retângulo({unidade_medida}): '))
    area = print(f'A área do retângulo é de {base*altura}{unidade_medida}²')
    return area

calculo_area_retangulo()