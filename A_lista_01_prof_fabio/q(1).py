vel = float(input("\nInforme a velocidade em m/s: "))

def conversao(velocidade):
    new_vel = velocidade * 3.6
    print(f'A velocidade de {vel:.1f}m/s ao ser convertida ficam em {new_vel:.1f}km/h\n')

conversao(vel)