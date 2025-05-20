# Entrada
valor = float(input('Valor: R$ '))
taxa = float(input('Taxa: '))
tempo = int(input('Tempo: '))

print('------------------------')
# Processamento
montante = valor + (valor * taxa * tempo)

# Saida
print(f'Montante Final: R${montante:.2f}')