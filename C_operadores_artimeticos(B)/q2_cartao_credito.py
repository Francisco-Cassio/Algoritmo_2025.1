def calcular_fatura(valor_fatura, valor_pagamento, meses):
    valor = ( valor_fatura - valor_pagamento)
    juros = (1 + juros_rotativo + multa_atraso + juros_mora)
    return valor * juros ** meses


def crescimento(saldo_final, valor_fatura, valor_p):
    crescimento = ((saldo_final - (valor_fatura - valor_p)) / (valor_fatura - valor_p)) * 100
    return crescimento


def linhas():
    return print('-----------------------------------')


valor_fatura = float(input('Valor Total da Fatura: R$ '))
linhas()
valor_p1 = float(input('Valor Pago no Plano 1: R$ '))
meses_p1 = int(input('Quantidade de Meses Sem Pagar no Plano 1: '))
linhas()
valor_p2 = float(input('Valor Pago no Plano 2: R$ '))
meses_p2 = int(input('Quantidade de Meses sem Pagar no Plano 2: '))

juros_rotativo = 0.12
multa_atraso = 0.02
juros_mora = 0.01

saldo_final_p1 = calcular_fatura(valor_fatura, valor_p1, meses_p1)
saldo_final_p2 = calcular_fatura(valor_fatura, valor_p2, meses_p2)

crescimento_p1 = crescimento(saldo_final_p1, valor_fatura, valor_p1)
crescimento_p2 = crescimento(saldo_final_p2, valor_fatura, valor_p2)

print('\n=======================================\n')

print(f'>>>>>>> PLANO 1 <<<<<<<\n\nValor Original da Dívida: R$ {valor_fatura - valor_p1:.2f}\nValor Final após {meses_p1} meses: R$ {saldo_final_p1:.2f}\nCrescimento da Dívida: {crescimento_p1:.2f}%\n')
print(f'>>>>>>> PLANO 2 <<<<<<<\n\nValor Original da Dívida: R$ {valor_fatura - valor_p2:.2f}\nValor Final após {meses_p2} meses: R$ {saldo_final_p2:.2f}\nCrescimento da Dívida: {crescimento_p2:.2f}%\n')

