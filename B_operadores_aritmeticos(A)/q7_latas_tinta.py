# Entrada
altura = float(input('Altura: '))
largura = float(input('Largura: '))

print('-------------------------')
# Processamento
latas = altura//largura

# Saida
print(f'Para uma área de {altura:.2f} m X {largura:.2f} m,\nserão necessários {latas:.0f} lata(s) de tinta')