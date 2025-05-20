import utils

def main():
    num = utils.get_integer_number('Número: ')
    utils.linhas()

    print(f'>>> FATORIAL DE {num} <<<\n')
    validar_valores(num)


def validar_valores(num: int):
    num_fat = num
    contador = 1
    fatorial = 1

    if num < 0:
        print('Não existe fatorial de número negativo!\nTente novamente...')
        utils.linhas()
        num = utils.get_integer_number('Número: ')
        utils.linhas()
        return validar_valores()
    
    elif num == 0:
        fatorial = 1

    else:
        fatorial = calcular_fatorial(num_fat, contador, fatorial)
        print(f'>>> {num}! = {fatorial}')


def calcular_fatorial(num: int, contador: int, fatorial: int):
    while num >= contador:
        fatorial *= num
        num -= 1
    return fatorial


main()