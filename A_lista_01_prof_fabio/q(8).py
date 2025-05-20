num1 = int(input("\nDigite um número: "))
num2 = int(input("Digite mais um número: "))

def calculo():
    div = (num1 + num2)/(num1 - num2)
    calc = print(f'{num1 + num2} / {num1 - num2} = {div:.1f}')
    return calc

calculo()