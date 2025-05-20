import utils

def main():
    preco_a = utils.get_decimal_number_min('Valor do Produto A: ', 0)
    preco_b = utils.get_decimal_number_min('Valor do Produto B: ', 0)
    preco_c = utils.get_decimal_number_min('Valor do Produto C: ', 0)
    utils.linhas()

    barato = 0

    if preco_a < preco_b and preco_a < preco_c:
        print(f'Melhor opção: Produto A')
    elif preco_b < preco_a and preco_b < preco_c:
        print(f'Melhor opção: Produto B')
    else:
        print(f'Melhor opção: Produto C')
    

main()