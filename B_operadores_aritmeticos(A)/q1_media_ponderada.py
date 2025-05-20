# Entrada
n1 = float(input('Primeira nota: '))
peso1 = int(input('Peso: '))

print('------------------------')

n2 = float(input('Segunda nota: '))
peso2 = int(input('Peso: '))

print('------------------------')

n3 = float(input('Terceira nota: '))
peso3 = int(input('Peso: '))

print('------------------------')

#Processamento
media_pond = (n1*peso1 + n2*peso2 + n3*peso3) / (peso1 + peso2 + peso3)

#Saida
print(f'Média ponderada: {media_pond:.2f}')