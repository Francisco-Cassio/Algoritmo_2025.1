def calculo():
    num = int(input("Digite um número de 4 dígitos: "))
    unidade_milhar = num//1000
    centena = (num%1000) // 100
    dezena = ((num % 1000) % 100) // 10
    unidade = num % 10
    print(f'{unidade_milhar} + {centena} + {dezena} + {unidade} = {unidade_milhar + centena + dezena + unidade}')

calculo()