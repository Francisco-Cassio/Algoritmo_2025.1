import utils

def main():
    carnes = '''
>>>>> CARNES DISPONÍVEIS <<<<<
\t\tAté 5 kg\tAcima de 5 kg
1 - Filé\tR$ 4,90 por Kg\tR$ 5,80 por Kg
2 - Alcatra\tR$ 5,90 por Kg\tR$ 6,80 por Kg
3 - Picanha\tR$ 6,90 por Kg\tR$ 7,80 por kg

Digite o número equivalente ao tipo de carne'''
    print(carnes)
    utils.linhas()

    tipo = utils.get_integer_number_min('Qual tipo de carne deseja? ', 1)
    qtd_carne = utils.get_integer_number_min('Quantidade de carne (em kg): ', 1)
    utils.linhas()

    if tipo == 1:
        tipo_carne = 'Filé'
        if qtd_carne <= 5:
            preco = qtd_carne * 4.9
        else:
            preco = qtd_carne * 5.8

    elif tipo == 2:
        tipo_carne = 'Alcatra'
        if qtd_carne <= 5:
            preco = qtd_carne * 5.9
        else:
            preco = qtd_carne * 6.8

    elif tipo == 3:
        tipo_carne = 'Picanha'
        if qtd_carne <= 5:
            preco = qtd_carne * 6.9
        else:
            preco = qtd_carne * 7.8
        
    cartao = input('A compra será feita utilizando o Cartão Tabajara (S/N)? ').upper()
    utils.limpar_tela()
    utils.linhas()

    if cartao == 'S':
        tipo_pagamento = 'Cartão Tabajara'
        desconto = preco * 0.05
        preco_desconto = preco - desconto
    else:
        tipo_pagamento = 'Espécie'
        desconto = 0
        preco_desconto = preco

    nota_fiscal = f'''>>>>> HIPERMERCADO TABAJARA <<<<<

Tipo da Carne: {tipo_carne}
Quantidade de carne: {qtd_carne} kg
-----------------------------------
Preço Total: R$ {preco:.2f}
Tipo de Pagamento: {tipo_pagamento}
Valor do Desconto: R$ {desconto:.2f}
-----------------------------------
Valor a Pagar: R$ {preco_desconto:.2f}
-----------------------------------'''

    print(nota_fiscal)


main()