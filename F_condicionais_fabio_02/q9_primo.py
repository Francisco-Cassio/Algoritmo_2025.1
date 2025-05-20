from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num = obter_numero_inteiro('Número entre 0 e 100: ')

    linhas()
    
    if intervalo(num):
        if eh_primo(num):
            print(f'O número {num} é primo')
        else:
            print(f'o número {num} não é primo')
    else:
        print('O número deve estar no intervalo de 0 a 100!')


def eh_primo(num: int):
    if num == 2:
        return True
    else:
        if num > 1:   
            for i in range(2, num):
                return num % i != 0


def intervalo(num):
    return num >= 0 and num <= 100
        

main()