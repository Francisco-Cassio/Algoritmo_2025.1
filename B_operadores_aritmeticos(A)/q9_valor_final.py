# Entrada
valor = float(input('Valor: R$ '))
desconto = int(input('Desconto: '))

print('--------------------------')
# Processamento
valor_final = valor - (valor * (desconto / 100))

# Saida
print(f'O valor com desconto será de\n>>>>>>>> R${valor_final:.2f} <<<<<<<<')
