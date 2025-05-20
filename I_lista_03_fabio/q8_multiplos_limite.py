import utils

def main():
    n = utils.get_integer_number('Valor de N: ')
    utils.linhas()
    limite_inf = utils.get_integer_number_min('Limite Inferior: ', 0)
    limite_sup = utils.get_integer_number_min('Limite Superior: ', 0)
    utils.linhas()

    validar_valores(n, limite_inf, limite_sup)
    

def validar_valores(n: int, lim_inf: int, lim_sup: int):
    if n > 0:
        maior = lim_sup
        if lim_sup < lim_inf:
            lim_sup = lim_inf
            lim_inf = maior
            return validar_valores(n, lim_inf, lim_sup)

        elif lim_inf == lim_sup:
            print('Os limites não podem ser iguais!\nTente novamente...')
            utils.linhas()
            lim_inf = utils.get_integer_number('Limite Inferior: ')
            lim_sup = utils.get_integer_number('Limite Superior: ', 0)
            utils.linhas()
            return validar_valores(n, lim_inf, lim_sup)
        
        else:
            if n < lim_inf or n > lim_sup:
                print('O valor deve estar dentro dos limites!\nTente novamente...')
                utils.linhas()
                lim_inf = utils.get_integer_number('Limite Inferior: ')
                lim_sup = utils.get_integer_number('Limite Superior: ')
                utils.linhas()
                return validar_valores(n, lim_inf, lim_sup)
            
            else:
                verificar_multiplos(n, lim_inf, lim_sup)
    
    elif n == 0:
        print('Apenas 0 é múltiplo de 0!')
        utils.linhas()

    else:
        print('O valor de N deve ser positivo!\nTente novamente...')
        utils.linhas()
        n = utils.get_integer_number('Valor de N: ')
        utils.linhas()
        return validar_valores(n, lim_inf, lim_sup)


def verificar_multiplos(n: int, lim_inf: int, lim_sup: int):
    while lim_inf <= lim_sup:
        if lim_inf % n == 0:
            print(f'{lim_inf} é múltiplo de {n}')
        lim_inf += 1
    utils.linhas()


main()