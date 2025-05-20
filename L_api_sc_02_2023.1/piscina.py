import utils

def main():
    print('OBS: os valores devem estar em cm (centímetros)!')
    largura = utils.get_decimal_number_min('Largura da piscina: ', 1)
    comprimento = utils.get_decimal_number_min('Comprimento da piscina: ', 1)
    profundidade = utils.get_decimal_number_min('Profundidade da piscina: ', 1)

    litros = (largura * comprimento * profundidade) / 1000
    quantidade_ideal = litros * 0.85

    valor_por_mil = utils.get_decimal_number_min('Valor pago por cada 1000L: R$ ', 1)

    valor_pago = valor_por_mil * calcular_valor_litro(litros)
    valor_mensal = valor_pago * 0.1

    resultado = f'''>>>>> JORGE PISCINA'S <<<<<
-----------------------------------
Capacidade máxima da piscina: {litros}L
Quantidade ideal: {quantidade_ideal}L
-----------------------------------
Valor necessário para encher a piscina: R$ {valor_pago:.2f}
valor necessário para repor mensalmente: R$ {valor_mensal:.2f}
-----------------------------------
'''
    utils.limpar_tela()
    print(resultado)


def calcular_valor_litro(litros: float):
    if litros % 1000 == 0:
        return litros // 1000
    else:
        return (litros // 1000) + 1


main()