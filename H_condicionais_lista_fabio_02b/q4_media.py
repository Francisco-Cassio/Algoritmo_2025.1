import utils

def main():
    nota_a = utils.get_decimal_number_min('Nota A: ', 0)
    nota_b = utils.get_decimal_number_min('Nota B: ', 0)
    utils.linhas()

    media = (nota_a + nota_b) / 2
    print(f'Média: {media:.2f}')
    
    if media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')


main()