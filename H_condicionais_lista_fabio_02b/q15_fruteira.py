import utils

def main():
    qtd_morango = utils.get_integer_number_min('Quantidade de morangos (em kg): ', 1)
    qtd_macas = utils.get_integer_number_min('Quantidade de maçãs (em kg): ', 1)
    utils.linhas()

    if qtd_morango <= 5:
        preco_morango = qtd_morango * 2.5
    else:
        preco_morango = qtd_morango * 2.2

    if qtd_macas <= 5:
        preco_macas = qtd_macas * 1.8
    else:
        preco_macas = qtd_macas * 1.5

    peso_total = qtd_morango + qtd_macas
    preco_total = preco_morango + preco_macas

    if peso_total >= 8 or preco_total > 25:
        preco_total = preco_total - (preco_total * 0.1)
    
    print(f'O valor a ser pago será de R$ {preco_total:.2f}')


main()