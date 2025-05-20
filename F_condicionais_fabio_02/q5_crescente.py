from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    n1 = obter_numero_inteiro('Primeiro Número: ')
    n2 = obter_numero_inteiro('Segundo Número: ')
    n3 = obter_numero_inteiro('Terceiro Número: ')

    maior = eh_maior(n1, n2, n3)
    meio = valor_do_meio(n1, n2, n3)
    menor = eh_menor(n1, n2, n3)

    linhas()
    print(f'Em ordem crescente temos:\n===== {menor} -> {meio} -> {maior} =====')


def eh_maior(n1: int, n2: int, n3: int):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    return maior


def valor_do_meio(n1: int, n2: int, n3: int):
    meio = n1
    if meio < n2 < n3 or n3 < n2 < meio:
        meio = n2
    elif meio < n3 < n2 or n2 < n3 < meio:
        meio = n3

    return meio


def eh_menor(n1: int, n2: int, n3: int):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    return menor


main()