num = int(input("Digite um número(3 digitos): "))

def soma_elementos():
    centena = num//100
    dezena = (num%100)//10
    unidade = (num%100)%10
    soma = print(f'{centena} + {dezena} + {unidade} = {centena + dezena + unidade}')
    return soma

soma_elementos()