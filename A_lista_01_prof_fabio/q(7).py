num1 = int(input("\nDigite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))



def calculo():
    soma2 = num1 + num2
    diferenca2 = num2 - num3
    calc = print(f'{num1:.0f} + {num2:.0f} = {soma2:.0f}\n{num2:.0f} - {num3:.0f} = {diferenca2:.0f}')
    return calc

calculo()