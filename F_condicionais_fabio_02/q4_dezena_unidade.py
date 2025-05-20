from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num = obter_numero_inteiro('Número: ')

    linhas()
    print('A dezena e a unidade possuem:')
    if dezena_igual_unidade(num):
        print('>>>>>>> O MESMO VALOR <<<<<<<')
    else:
        print('>>>> VALORES DIFERENTES <<<<')

def dezena_igual_unidade(num: int):
    dezena = num // 10
    unidade = num % 10

    return dezena == unidade
    

main()