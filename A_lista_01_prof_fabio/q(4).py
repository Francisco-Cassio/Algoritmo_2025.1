valor_do_dolar = float(input("Informe o valor do dólar em reais: "))
valor_em_dolar = float(input("Informe a quantia em dólar que possui: "))

def conversao():
    valor_em_real = print(f'{valor_em_dolar:.2f} dólares é equivalente a {valor_em_dolar * valor_do_dolar:.2f} reais')
    return valor_em_real

conversao()
