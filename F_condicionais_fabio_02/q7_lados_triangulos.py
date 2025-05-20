from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    lado_a = obter_numero_inteiro('Primeiro Lado: ')
    lado_b = obter_numero_inteiro('Segundo Lado: ')
    lado_c = obter_numero_inteiro('Terceiro Lado: ')

    linhas()

    if tamanho_zero(lado_a, lado_b, lado_c):
        print('Não existe lado com tamanho 0')
    else:
        if eh_triangulo(lado_a, lado_b, lado_c):
            print('Esta forma é um triângulo')
            if eh_equilatero(lado_a, lado_b, lado_c):
                print('====> E é um EQUILÁTERO')
            elif eh_isosceles(lado_a, lado_b, lado_c):
                print('====> E é um ISÓSCELES')
            elif eh_escaleno(lado_a, lado_b, lado_c):
                print('====> E é um ESCALENO')
        else:
            print('Esta forma não é um triângulo')

        
def eh_triangulo(a: int, b: int, c: int):
    return a <= b + c and b <= a + c and c <= a + b


def eh_equilatero(a: int, b: int, c: int):
    return a == b == c


def eh_isosceles(a: int, b: int, c: int):
    return a == b or b == c or a == c and not eh_equilatero(a, b, c)


def eh_escaleno(a: int, b: int, c: int):
    return a != b != c


def tamanho_zero(a: int, b: int, c: int):
    return a == 0 or b == 0 or c == 0


main()