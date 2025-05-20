import utils

def main():
    n = utils.get_integer_number_min('Quantidade de valores: ', 1)
    utils.linhas()

    validar_valores(n)
    

def validar_valores(qtd_num: int):
    contador = 1
    soma = 0

    while contador <= qtd_num:
        num = utils.get_integer_number_min('Digite um valor: ', 0)
        soma += num
        contador += 1

    utils.linhas()
    media = calculo_media(soma, qtd_num)

    print(f'Soma dos valores: {soma}\nMédia dos valores: {media:.2f}')
    utils.linhas()


def calculo_media(soma: int, qtd: int):
    return soma / qtd


main()