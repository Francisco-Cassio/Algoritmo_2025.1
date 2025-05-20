def calculo():
    num_a = int(input("Digite o número A: "))
    num_b = int(input("Digite o número B: "))
    num_c = int(input("Digite o número C: "))

    R = (num_a + num_b)**2
    S = (num_b + num_c)**2
    D = (R + S)/2
    print(f'Levando em conta que R = (A+B)², S = (B+C)², e D = R+S/2, o valor de D será {D:.0f}')

calculo()