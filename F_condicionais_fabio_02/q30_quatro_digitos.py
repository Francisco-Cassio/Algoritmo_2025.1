from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num = obter_numero_inteiro('Valor de 4 dígitos: ')

    linhas()

    soma = valor_soma(num)
    quadrado = valor_quadrado(num)

    if num == quadrado:
        print(f'Soma: {soma}')
        print(f'Quadrado da soma: {quadrado}')
        linhas()
        print(f'{num} = {quadrado}: os valores se correspondem')
    else:
        print(f'Soma: {soma}')
        print(f'Quadrado da soma: {quadrado}')
        linhas()
        print(f'{num} ≠ {quadrado}: os valores não se correspondem')
        

def valor_soma(num: int):
    return (num // 100) + (num % 100)


def valor_quadrado(num: int):
    return valor_soma(num) ** 2
    

main()