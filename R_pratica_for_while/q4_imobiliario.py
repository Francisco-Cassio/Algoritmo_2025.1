# 4. Imobiliário: Análise de Retorno de Investimento em Alugueis

# ● Contexto/Problema: Um investidor imobiliário quer analisar o retorno de investimento (ROI) de múltiplos imóveis alugados ao longo de um período. Para cada imóvel, o programa deve permitir que o usuário insira o valor de compra do imóvel, o valor do aluguel mensal e o número de anos que o imóvel foi alugado. O programa deve calcular o retorno total (soma dos aluguéis recebidos menos o valor de compra) e a taxa de retorno anualizada para cada imóvel. Ao final, deve indicar qual imóvel gerou o maior retorno total e a maior taxa de retorno anualizada.

# ● Entrada: O usuário deve informar a quantidade de imóveis a serem analisados. Para cada imóvel, o usuário deve informar o valor de compra, o valor do aluguel mensal e o número de anos que o imóvel esteve alugado.

# ● Saída Esperada: Para cada imóvel, o retorno total e a taxa de retorno anualizada. Ao final, indicar o imóvel (pelo seu número ou identificador) com o maior retorno total e o imóvel com a maior taxa de retorno anualizada.

def main():
    qtd_imoveis = int(input('Quantidade de imóveis: '))

    maior_retorno = None
    maior_taxa = None

    for i in range(1, qtd_imoveis + 1, 1):
        valor_compra = float(input('Valor da compra: R$ '))
        valor_aluguel = float(input('Valor do aluguel: R$ '))
        anos = int(input('Número de anos: '))

        retorno_total = ((valor_aluguel * 12) * anos) - valor_compra

        taxa_retorno = retorno_total / anos
        retorno_anual = (taxa_retorno * 100) / valor_compra

        if maior_taxa == None or taxa_retorno > maior_taxa:
            maior_taxa = taxa_retorno

        if maior_retorno == None or retorno_total > maior_retorno:
            maior_retorno = retorno_anual

        resultado = f'''
Retorno total: R$ {retorno_total:.2f}
Taxa de retorno anualizada: {retorno_anual:.2f}%'''
        
        print(resultado)
    
    print(f'\nMaior retorno total: R$ {maior_retorno:.2f}\nMaior taxa de retorno anualizada: {maior_taxa}')





main()