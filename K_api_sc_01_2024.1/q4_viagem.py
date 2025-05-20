import utils

def main():
    utils.limpar_tela()
    origem = input('Local de saída: ')
    destino = input('Destino final: ')
    utils.linhas()
    valor_rs = utils.get_decimal_number_min('Valor em R$ no site: R$ ', 1)
    valor_milhas = utils.get_integer_number_min('Valor em Milhas no site: ', 1)
    utils.linhas()

    avalicao_precos(valor_rs, valor_milhas)


def avalicao_precos(valor_rs: float, valor_milhas: int):
    milhas_padrao = (valor_milhas / 1000) * 70
    milhas_baratas = (valor_milhas / 1000) * 14.50

    porcentagem_mp = (milhas_padrao / valor_rs) * 100
    porcentagem_mb = (milhas_baratas / valor_rs) * 100

    print(f'O valor em Milhas Padrão equivale a {porcentagem_mp:.2f}% do valor em R$')
    print(f'O valor em Milhas Baratas equivale a {porcentagem_mb:.2f}% do valor em R$')
    utils.linhas()

    comparacao = f'''
=> Milhas Padrão: R$ {milhas_padrao:.2f}
=> Milhas Baratas: R$ {milhas_baratas:.2f}
=> Valor em Reais: R$ {valor_rs:.2f}
'''
    
    print(comparacao)
    utils.linhas()

    if milhas_padrao < milhas_baratas and milhas_padrao < valor_rs:
        print('A melhor opção é de Milhas Padrão')

    elif milhas_baratas < milhas_padrao and milhas_baratas < valor_rs:
        print('A melhor opção é de Milhas Baratas')
    
    else:
        print('>>> A melhor opção é o Valor em R$')

    utils.linhas()


main()