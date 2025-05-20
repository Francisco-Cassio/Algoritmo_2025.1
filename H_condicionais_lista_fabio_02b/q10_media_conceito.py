import utils

def main():
    nota_a = utils.get_decimal_number_min('Nota A: ', 0)
    nota_b = utils.get_decimal_number_min('Nota B: ', 0)
    utils.linhas()

    media = (nota_a + nota_b) / 2
    conceito = ''

    if media >= 9 and media <= 10:
        conceito = 'A'
    elif media >= 7.5:
        conceito = 'B'
    elif media >= 6:
        conceito = 'C'
    elif media >= 4:
        conceito = 'D'
    else:
        conceito = 'E'

    if conceito in ('A', 'B', 'C'):
        print(f'Conceito: {conceito}\nSituação: APROVADO')
    else:
        print(f'Conceito: {conceito}\nSituação: REPROVADO')  
    utils.linhas()


main()