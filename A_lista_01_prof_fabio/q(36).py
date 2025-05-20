def calculo():
    anos = int(input("\nDigite sua idade em anos: "))
    meses = int(input("Digite os meses de idade: "))
    dias = int(input("Digite os dias de idade: "))
    dias_anos = anos * 365
    dias_meses = meses * 30
    print(f'{anos} ano(s) {meses} mese(s) e {dias} dia(s) corresponde a {(anos*365) +(meses*30) + dias} dia(s)')

calculo()