import utils

def main():
    qtd_habitantes = utils.get_integer_number_min('Quantidade de habitantes: ', 1)
    utils.linhas()

    print('\n>>> AVALIAÇÃO SOCIOECONÔMICA <<<')
    utils.linhas()
    pesquisa_economica(qtd_habitantes)


def pesquisa_economica(n: int):
    contador = 1
    soma_salario = 0
    soma_filhos = 0
    menor_mil = 0

    while contador <= n:
        print(f'\n>>> HABITANTE N° {contador}:\n')
        salario = utils.get_decimal_number('Salário: ')
        qtd_filhos = utils.get_integer_number_min('Quantidade de filhos: ', 0)
        utils.linhas()

        soma_salario += salario
        soma_filhos += qtd_filhos

        if salario <= 1000:
            menor_mil += 1

        contador += 1

    media_salario = calcular_media(soma_salario, n)
    media_filhos = calcular_media(soma_filhos, n)

    percentual = (menor_mil / n) * 100

    print(f'\n>>> MÉDIA DE SALÁRIOS: R$ {media_salario:.2f}\n>>> MÉDIA DE FILHOS: {media_filhos:.0f}\n>>> PERCENTUAL DE PESSOAS COM SALÁRIO <= R$ 1000.00: {percentual:.2f}%')
    utils.linhas()

def calcular_media(soma: int, n: int):
    return soma / n


main()