def juros_compostos(valor, taxa, tempo):
    return valor * (1 + (taxa / 100)) ** tempo


def valor_parcela(montante, tempo):
    return montante / tempo


def linhas():
    return print('-----------------------------------')


valor = float(input('Valor: R$ '))
linhas()
taxa_cdb = int(input('Taxa de Juros Anual (Entre 1% a 20%): '))
tempo_cdb = int(input('Tempo de Investimento (Anos): '))

valor_cdb = juros_compostos(valor, taxa_cdb, tempo_cdb)

linhas()

taxa_cdc = int(input('Taxa de Juros Mensal (Entre 1% a 17%): '))
tempo_cdc = int(input('Número de Parcelas do Empréstimo (24x, 36x ou 60x): '))

valor_cdc = juros_compostos(valor, taxa_cdc, tempo_cdc)
parcela_cdc = valor_parcela(valor_cdc, tempo_cdc)

lucro_banco = valor_cdc - valor_cdb

print('\n=======================================\n')

print(f'Valor de Investimento (CDB): R$ {valor:.2f}\nValor de Pagamento ao Investidor: {valor_cdb:.2f}\n')
linhas()
print(f'Valor do Empréstimo (CDC): R$ {valor:.2f}\nValor Pago pelo Cliente: R$ {valor_cdc:.2f}\nValor da Parcela (CDC): R$ {parcela_cdc:.2f}\n\n>>>>>>>>>> Lucro do Banco: R$ {lucro_banco:.2f}')