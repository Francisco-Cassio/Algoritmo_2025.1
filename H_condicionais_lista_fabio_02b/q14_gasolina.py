import utils

def main():
    qtd_litros = utils.get_integer_number_min('Quantos litros deseja? ', 1)
    tipo_combustivel = input('Será álcool ou gasolina (A ou G)? ').upper()
    utils.linhas()

    if tipo_combustivel == 'A':
        if qtd_litros <= 20:
            desconto = qtd_litros * (qtd_litros * 0.03)

        elif qtd_litros > 20:
            desconto = qtd_litros * (qtd_litros * 0.03)

        preco = (qtd_litros * 1.9) - desconto
        print(f'O valor a ser pago será R$ {preco:.2f}')
    
    elif tipo_combustivel == 'G':
        if qtd_litros <= 20:
            desconto = qtd_litros * (qtd_litros * 0.04)

        elif qtd_litros > 20:
            desconto = qtd_litros * (qtd_litros * 0.06)

        preco = (qtd_litros * 2.5) - desconto
        print(f'O valor a ser pago será R$ {preco:.2f}')

    else:
        print('Valor Inválido!')

main()