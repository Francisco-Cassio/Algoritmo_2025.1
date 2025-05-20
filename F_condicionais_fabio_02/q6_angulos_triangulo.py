from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    angulo_a = obter_numero_inteiro('Primeiro Ângulo Interno: ')
    angulo_b = obter_numero_inteiro('Segundo Ângulo Interno: ')
    angulo_c = obter_numero_inteiro('Terceiro Ângulo Interno: ')

    linhas()

    if angulo_zero(angulo_a, angulo_b, angulo_c):
        print('Não existe lado com tamanho 0°')
    else:
        if eh_triangulo(angulo_a, angulo_b, angulo_c):
            print('Esta forma é um triângulo')
            if eh_acutangulo(angulo_a, angulo_b, angulo_c):
                print('====> E é um ACUTÂNGULO')
            elif eh_retangulo(angulo_a, angulo_b, angulo_c):
                print('====> E é um RETÂNGULO')
            elif eh_obtusangulo(angulo_a, angulo_b, angulo_c):
                print('====> E é um OBTUSÂNGULO')
        else:
            print('Esta forma não é um triângulo')

        
def eh_triangulo(a: int, b: int, c: int):
    return a + b + c == 180


def eh_acutangulo(a: int, b: int, c: int):
    return a < 90 and b < 90 and c < 90


def eh_retangulo(a: int, b: int, c: int):
    return a == 90 or b == 90 or c == 90


def eh_obtusangulo(a: int, b: int, c: int):
    return a > 90 or b > 90 or c > 90


def angulo_zero(a: int, b: int, c: int):
    return a == 0 or b == 0 or c == 0


main()