import utils

def main():
    n = utils.get_integer_number_min('Quantidade de números: ', 0)
    utils.linhas()

    verificar_maior(n)


def verificar_maior(n: int):
    contador = 1
    maior = 0

    while contador <= n:
        num = utils.get_integer_number_min('Digite um valor: ', 0)
        if num > maior:
            maior = num
        contador += 1
    
    utils.linhas()
    print(f'>>> MAIOR VALOR: {maior} <<<')
    utils.linhas()
    

main()