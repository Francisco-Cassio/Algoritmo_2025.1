def calculo_area_quadrado():
    unidade_medida = input("Informe a unidade de medida: ")
    lado = float(input(f'Informe o valor do lado do quadrado({unidade_medida})'))
    area = lado**2
    print(f'A área do quadrado é de {area}{unidade_medida}²')

calculo_area_quadrado()