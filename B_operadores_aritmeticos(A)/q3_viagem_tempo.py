# Entrada
distancia = float(input('Qual a distância da viagem? '))
velocidade = float(input('Qual a velocidade? '))

print('-----------------------------------')
# Processamento
tempo = distancia / velocidade
hora = tempo // 60
minuto = tempo % 60

# Saida
print(f'O tempo que a viagem levará será: {tempo:.1f} km/h')
