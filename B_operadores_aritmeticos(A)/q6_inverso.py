# Entrada
num = int(input('Número: '))

print('-------------')
# Processamento
centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

# Saida
print(f'Inverso: {unidade}{dezena}{centena}')