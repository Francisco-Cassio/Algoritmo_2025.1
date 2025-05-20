import utils

def main():
    limite_inf = utils.get_integer_number_min('Limite Inferior: ', 0)
    limite_sup = utils.get_integer_number_min('Limite superior: ', 0)
    utils.linhas()

    validar_valores(limite_inf, limite_sup)


def validar_valores(lim_inf: int, lim_sup: int):
    maior = lim_sup
    if lim_inf > lim_sup:
        lim_sup = lim_inf
        lim_inf = maior
        return validar_valores(lim_inf, lim_sup)
    
    elif lim_inf == lim_sup:
        print('Os limites devem ter valores diferentes!\nTente novamente...')
        utils.linhas()
        lim_inf = utils.get_integer_number_min('Limite Inferior: ', 0)
        lim_sup = utils.get_integer_number_min('Limite superior: ', 0)
        utils.linhas()
        return validar_valores(lim_inf, lim_sup)
    
    else:
        print('>>> NÚMEROS ÍMPARES <<<\n')
        calcular_impar(lim_inf, lim_sup)
        utils.linhas()


def calcular_impar(lim_inf: int, lim_sup: int):
   while lim_inf <= lim_sup:
        if lim_inf % 2 != 0:
            print(f'{lim_inf} é ímpar')
        lim_inf += 1


main()