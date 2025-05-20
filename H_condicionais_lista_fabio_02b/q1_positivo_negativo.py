import utils

def main():
    num = utils.get_integer_number('Digite um valor: ')
    utils.linhas()

    if num == 0:
        print(f'O valor {num} é zero')
    elif num > 0:
        print(f'{num} é positivo')
    else:
        print(f'{num} é negativo')


main()