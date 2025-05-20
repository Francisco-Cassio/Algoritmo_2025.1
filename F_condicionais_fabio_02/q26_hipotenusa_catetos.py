from funcoes import obter_numero_real
from funcoes import linhas

def main():
    lado_a = obter_numero_real('Lado A: ')
    lado_b = obter_numero_real('Lado B: ')
    lado_c = obter_numero_real('Lado C: ')

    linhas()

    hipotenusa = eh_hipotenusa(lado_a, lado_b, lado_c)
    cateto_a = cateto_um(lado_a, lado_b, lado_c)
    cateto_b = cateto_dois(lado_a, lado_b, lado_c)

    print(f'Hipotenusa: {hipotenusa}\nCateto A: {cateto_a}\nCateto B: {cateto_b}')


def eh_hipotenusa(a: int, b: int, c: int):
    maior = a
    if b > maior:
        maior = b
        if c > maior:
            maior = c
    elif c > maior:
        maior = c
    
    return maior


def cateto_um(a: int, b: int, c: int):
    if eh_hipotenusa(a, b, c) == a:
        return b
    elif eh_hipotenusa(a, b, c) == b:
        return c
    else:
        return a
    

def cateto_dois(a: int, b: int, c: int):
    if eh_hipotenusa(a, b, c) == a:
        return c
    elif eh_hipotenusa(a, b, c) == b:
        return a
    else:
        return b


main()