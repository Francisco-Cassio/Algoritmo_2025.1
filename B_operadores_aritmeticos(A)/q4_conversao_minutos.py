# Entrada
min = int(input('Quantos minutos? '))

print('----------------------')
# Processamento
horas = min // 60
minutos = min % 60

# Saida
print(f'{min} minutos equivale a\n>>>>> {horas} hora(s) e {minutos} minuto(s) <<<<<')