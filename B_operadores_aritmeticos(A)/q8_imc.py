# Entrada
print('>>>>>> FICHA IMC <<<<<<')
print('-----------------------')
peso = int(input('Peso: '))
altura = float(input('Altura: '))

print('-----------------------')
# Processamento
imc = peso / (altura * altura)

# Saida
print(f'IMC: {imc:.2f}')