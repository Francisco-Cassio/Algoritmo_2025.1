import utils

def main():
    num = utils.get_decimal_number_min('Digite um valor: ', 0)
    utils.linhas()

    num *= 10

    if num % 10 == 0:
        print('Este número é inteiro!')
    else:
        print('Este número é decimal')


main()