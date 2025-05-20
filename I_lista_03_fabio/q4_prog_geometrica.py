import utils

def main():
    a0 = utils.get_integer_number('Limite Inicial: ')
    limite = utils.get_integer_number('Limite Final: ')
    utils.linhas()
    r = utils.get_integer_number('Razão da P.G: ')
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
        a0 = utils.get_integer_number('Limite Inicial: ')
        limite = utils.get_integer_number('Limite Final: ')
        utils.linhas()
        return validar_valores(a0, limite, r)
    
    if (a0 * r) < a0:
        print('O valor fugirá dos limites estabelecidos!\nTente novamente...')
        utils.linhas()
        r = utils.get_integer_number('Razão da P.G: ')
        utils.linhas()
        return validar_valores(a0, limite, r)
    
    else:
        if r > limite:
            print('A razão estar dentro dos limites!\nTente novamente...')
            utils.linhas()
            r = utils.get_integer_number('Razão da P.G: ')
            utils.linhas()
            return validar_valores(a0, limite, r)
    
    print('>>> PROGRESSÃO GEOMÉTRICA <<<')
    calcular_pg(a0, limite, r)


def calcular_pg(a0: int, limite: int, r: int):
    if a0 != 0:
        if r > 1:
            while a0 < limite:
                print(a0)
                a0 *= r

        elif r == 1 or r == 0:
            print(a0)

        else:
            while limite >= a0:
                print(limite)
                limite *= r
    else:
        print(a0)

            
    utils.linhas()
    
    
main()