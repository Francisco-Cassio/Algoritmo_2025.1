import utils

def main():
    num_dia = utils.get_decimal_number_min('Digite um número equivalente a um dia da semana: ', 1)
    utils.linhas()

    if num_dia == 1:
        print('Domingo')
    elif num_dia == 2:
        print('Segunda')
    elif num_dia == 3:
        print('Terça')
    elif num_dia == 4:
        print('Quarta')
    elif num_dia == 5:
        print('Quinta')
    elif num_dia == 6:
        print('Sexta')
    elif num_dia == 7:
        print('Sábado')
    else:
        print('Valor Inválido!')


main()