import utils

def main():
    num = utils.get_integer_number_min('Valor entre 1 e 999: ', 1)
    utils.linhas()

    if num > 99 and num <= 999:
        centena = num // 100
        dezena = (num % 100) // 10
        unidade = num % 10
        print(f'{centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')

    elif num > 9 and num <= 99:
        dezena = num // 10
        unidade = num % 10
        print(f'{dezena} dezena(s) e {unidade} unidade(s)')
    
    elif num >= 1 and num <= 9:
        unidade = num
        print(f'{unidade} unidade(s)')

    else:
        print('Valor Inválido!')


main()