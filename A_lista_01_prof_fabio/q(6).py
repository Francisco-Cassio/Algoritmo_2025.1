vel = float(input("\nInforme a velocidade(km/h): "))

def conversao():
    new_vel = print(f'{vel:.2f}km/h convertida equivale a {(vel/3.6):.2f}m/s')
    return new_vel

conversao()