from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    x1 = obter_numero_inteiro('Valor do 1° X: ')
    y1 = obter_numero_inteiro('Valor do 1° Y: ')
    linhas()
    x2 = obter_numero_inteiro('Valor do 2° X: ')
    y2 = obter_numero_inteiro('Valor do 2° Y: ')

    linhas()

    area = calcular_area(x1, x2, y1, y2)

    print(f'A área deste retângulo é: {area}')

def calcular_largura(x1: int, x2: int):
    if x1 > x2:
        return x1 - x2
    else:
        return x2 - x1
    

def calcular_altura(y1: int, y2: int):
    if y1 > y2:
        return y1 - y2
    else:
        return y2 - y1
    

def calcular_area(x1: int, x2: int, y1: int, y2: int):
    return calcular_largura(x1, x2) * calcular_altura(y1, y2)


main()