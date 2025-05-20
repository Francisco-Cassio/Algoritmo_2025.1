# Em 2021 o Brasil voltou a enfrentar crise na matriz energética devido ao baixo nível das águas nos reservatórios das hidrelétricas
# brasileiras. Devido a isso os consumidores deverão arcar com custos extras (bandeira) para bancar outras matrizes energéticas, como usinas
# termoelétricas. Neste mês de Junho a bandeira estabelecida pelo governo federal foi a Vermelha Patamar 2, que significa que a cada 100 KWh de
# consumo será acrescido uma taxa extra de R$ 8,00.
# O Cálculo da energia elétrica para o consumidor final é feito baseado em KWh e em faixas.
# Valores hipotéticos:

# ● Consumo de até 30KWh isento de tarifa.
# ● Até 100 KWh será cobrado R$ 0,59 por cada um cada de todo os KWh consumidos;
# ● acima de 100KWh o valor de R$ 0,75 por cada um de todos os KWh consumidos.

# Sobre o valor tarifado/apurado são 25% de ICMS e 15% de PIS/CONFIS.
# A taxa de iluminação pública é cobrada apenas para os consumidores que passarem de 80 KWh por mês, e custa 6% do valor tarifado (antes do
# impostos).
# Considerando os dados acima construa um software que receba dois dados:
# Leitura Atual e Leitura Anterior do medidor de energia e faça todo o cálculo do "Talão de Energia" conforme detalhado acima.
# Como saída apresente os dados que compõem assim como o valor total a ser pago.
# Exemplo:
# Consumo 000 KWh
# Valor Faturado R$ 0,00
# Bandeira R$ 0,00 (x bandeiras)
# ICMS R$ 0,00
# PIS/CONFIS
# Taxa Iluminação R$ 0,00

import utils

def main():
    leitura_anterior = utils.get_decimal_number_min('Leitura anterior (KWh): ', 0)
    leitura_atual = utils.get_decimal_number_min('Leitura atual (KWh): ', 0)
    consumo = leitura_atual - leitura_anterior if leitura_atual > leitura_anterior else leitura_anterior - leitura_atual
    utils.linhas()

    if consumo <= 30:
        valor_energia = 0
    elif consumo <= 100:
        valor_energia = consumo * 0.59
    else:
        valor_energia = consumo * 0.75

    bandeira = (consumo // 10) * 8
    
    taxa_iluminacao = valor_energia * 0.06 if consumo >= 80 else 0

    icms = (valor_energia + bandeira) * 0.25
    pis_confis = (valor_energia + bandeira) * 0.15

    valor = bandeira + valor_energia + icms + pis_confis + taxa_iluminacao

    print(f'''>>> TALÃO DE ENERGIA <<<
-----------------------------------
Consumo: {consumo} KWh
Valor Faturado: R$ {valor:.2f}
Bandeira: R$ {bandeira:.2f} (x bandeiras)
ICMS: R$ {icms:.2f}
PIS/CONFIS: R$ {pis_confis:.2f}
Taxa Iluminação: R$ {taxa_iluminacao:.2f}
-----------------------------------''')

main()