# 10. Clima e Tempo: Análise de Tendências de Temperatura ao Longo de Anos

# ● Contexto/Problema: Um pesquisador climático deseja analisar as tendências de temperatura máxima
# anual ao longo de uma série de anos. O programa deve permitir que o usuário insira o número de anos
# para os quais os dados serão registrados. Para cada ano, o usuário deve informar a temperatura
# máxima média anual. O programa deve identificar o ano com a maior temperatura, o ano com a menor
# temperatura, e calcular a média das temperaturas anuais. Além disso, deve indicar se houve uma
# tendência de aquecimento (se a média dos últimos anos for maior que a média dos primeiros anos).

# ● Entrada: O usuário deve informar a quantidade de anos para análise. Para cada ano, o usuário deve
# informar a temperatura máxima média anual.

# ● Saída Esperada: O ano (ou índice do ano) com a maior temperatura, o ano (ou índice do ano) com a
# menor temperatura, e a média geral das temperaturas anuais. Uma mensagem indicando se há uma
# tendência de aquecimento ou resfriamento baseada na comparação das médias da primeira e segunda
# metades dos anos.


def main():
    qtd_anos = int(input('Quantidade de anos: '))

    ano_mais_quente = None
    ano_menos_quente = None
    temp_mais_quente = None
    temp_menos_quente = None
    soma = 0


    for ano in range(1, qtd_anos + 1, 1):
        print(f'\n{ano}º ano:')
        temp = float(input(f'Temperatura máxima média anual: '))
        soma += temp

        if ano_mais_quente == None or temp > temp_mais_quente:
            temp_mais_quente = temp
            ano_mais_quente = ano

        if ano_menos_quente == None or temp < temp_menos_quente:
            temp_menos_quente = temp
            ano_menos_quente = ano

    media = soma / qtd_anos

    res = f'''
Ano com maior temperatura: {ano_mais_quente}º ano
Ano com menor temperatura: {ano_menos_quente}º ano
Média das temperaturas anuais: {media:.1f} °C
'''

    print(res)


main()