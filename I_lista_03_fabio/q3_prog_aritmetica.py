import utils

def main():
    a0 = utils.get_integer_number('Limite inicial: ')
    limite = utils.get_integer_number('Limite final: ')
    utils.linhas()
    r = utils.get_integer_number('Razão da P.A: ')
    utils.linhas()
    
    validar_valores(a0, limite, r)


def validar_valores(a0: int, limite: int, r: int):
    maior = limite
    if a0 > limite:
        limite = a0
        a0 = maior
        return validar_valores(a0, limite, r)
    
    elif a0 == limite:
        print('Os limites devem ter valores diferentes\nTente novamente...!')
        utils.linhas()
        a0 = utils.get_integer_number('Limite inicial: ')
        limite = utils.get_integer_number('Limite final: ')
        utils.linhas()
        return validar_valores(a0, limite, r)
    
    else:
        if r > limite:
            print('A razão estar dentro dos limites!\nTente novamente...')
            utils.linhas()
            r = utils.get_integer_number_min('Razão da P.A: ', 1)
            utils.linhas()
            return validar_valores(a0, limite, r)

    print('>>> PROGRESSÃO ARITMÉTICA <<<') 
    calcular_pa(a0, limite, r)


def calcular_pa(a0: int, limite: int, r: int):
    if r > 0:
        while a0 < limite:
            print(a0)
            a0 += r
    elif r < 0:
        limite -= 1
        while limite >= a0:
            print(limite)
            limite += r
    else:
        print(a0)

    utils.linhas()


main()