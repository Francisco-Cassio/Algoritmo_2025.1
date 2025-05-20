def calculo_area_triangulo():
    unidade_medida = input("Informe a unidade de medida: ")
    base = float(input(f'Informe a base do triângulo({unidade_medida}): '))
    altura = float(input(f'Informe a altura do triângulo({unidade_medida}): '))
    area = (base*altura)/2
    print(f'A área do triângulo é de {area}{unidade_medida}²')

calculo_area_triangulo()