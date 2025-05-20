def calculo():
    num = int(input("Digite um número: "))
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = num % 10
    new_number = (unidade*100) + (dezena*10) + (centena)
    print(f'{num} + {new_number} = {num + new_number}')

calculo()