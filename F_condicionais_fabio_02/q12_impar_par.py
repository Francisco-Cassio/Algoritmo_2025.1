from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num = obter_numero_inteiro('Valor: ')

    linhas()

    if eh_par_ou_impar(num):
        print(f'O valor {num} é PAR')
    else:
        print(f'O valor {num} é ÍMPAR')

def eh_par_ou_impar(num):
    return num % 2 == 0


main()