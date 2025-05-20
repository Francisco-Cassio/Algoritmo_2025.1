def calculo_comprimento_circunferencia():
    pi = float(input("Informe o valor de PI: "))
    unidade_medida = input("Informe a unidade de medida: ")
    raio_circunferencia = float(input(f'Informe o valor do raio da circunferência({unidade_medida}): '))
    comprimento = print(f'O raio da circunferência é de {(2*pi*raio_circunferencia):.2f}{unidade_medida}')
    return comprimento

calculo_comprimento_circunferencia()