def quantidade_gasolina(distancia_percorrida, percentual_motor_eletrico):
    distancia = distancia_percorrida + (distancia_percorrida * (percentual_motor_eletrico / 100))
    quantidade_litros = distancia / 12 # Neste cenário, 1 litro de gasolina equivale a 12 km
    return quantidade_litros


def quantidade_alcool(distancia_percorrida, percentual_motor_eletrico):
    distancia = distancia_percorrida + (distancia_percorrida * (percentual_motor_eletrico / 100))
    quantidade_litros = distancia / 10 # Neste cenário, 1 litro de álcool equivale a 10 km
    return quantidade_litros


def custo(quantidade_litros, valor_litro):
    custo = quantidade_litros * valor_litro
    return custo


def linhas():
    return print('--------------------------------------')

print('>>>>>>>>>> VIAGEM DE FÉRIAS <<<<<<<<<<')
linhas()
distancia_percorrida = float(input('Distância Total Prevista para a Viagem (km): '))
valor_litro_alcool = float(input('Valor do Litro de Álcool: R$ '))
valor_litro_gasolina = float(input('Valor do Litro de Gasolina: R$ '))
percentual_motor_eletrico = int(input('Quantos % da Viagem Serão Feitas com o Motor Elétrico: '))

print('\n======================================\n')

litros_gasolina = quantidade_gasolina(distancia_percorrida,  percentual_motor_eletrico)
litros_alcool = quantidade_alcool(distancia_percorrida, percentual_motor_eletrico)

custo_gasolina = custo(litros_gasolina, valor_litro_gasolina)
custo_alcool = custo(litros_alcool, valor_litro_alcool)

print(f'Serão necessários {litros_gasolina:.1f} L de gasolina para completar a viagem.\nIsto resultará em um total de R$ {custo_gasolina:.2f}.')
linhas()
print(f'Serão necessários {litros_alcool:.1f} L de álcool para completar a viagem.\nIsto resultará em um total de R$ {custo_alcool:.2f}')
linhas()