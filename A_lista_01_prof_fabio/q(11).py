
def inverso():
    num = int(input("\nDigite um número(3 dígitos): "))
    centena = num//100
    dezena = (num%100)//10
    unidade = (num%100)%10
    print(f'Número: {num}\nSeu inverso: {unidade}{dezena}{centena}')

inverso()