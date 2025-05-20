def calculo():
    dias = int(input("Digite seus dias de vida: "))
    anos = dias // 365
    meses = (dias%365) // 30
    new_dias = (dias%365) % 30
    print(f'{dias} dia(s) equivale a {anos} anos {meses} meses e {new_dias} dias')

calculo()