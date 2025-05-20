from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    medida = obter_numero_inteiro('Medida do ângulo: ')

    linhas()

    quadrante = verificar_quadrante(medida)

    if quadrante == 1:
        print(f'{medida}° está no {quadrante}° Quadrante')
    elif quadrante == 2:
        print(f'{medida}° está no {quadrante}° Quadrante')
    elif quadrante == 3:
        print(f'{medida}° está no {quadrante}° Quadrante')
    else:
        print(f'{medida}° está no {quadrante}° Quadrante')


def verificar_quadrante(medida: int):
    if 0 <= medida <= 90:
        return 1
    elif medida <= 180:
        return 2
    elif medida <= 270:
        return 3
    else:
        return 4
    

main()