# Entrada
valor = float(input('Valor: '))

print('------------------------')
# Processamento
cinquenta = valor // 50
dez = (valor % 50) // 10

# Saida
print(f'O valor de R${valor:.2f} pode ser pago com\n>>>> {cinquenta:.0f} nota(s) de 50 e\n>>>> {dez:.0f} nota(s) de 10')