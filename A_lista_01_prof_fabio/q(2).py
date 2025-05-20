
hora = int(input("Informe as horas: "))
min = int(input("Informe os minutos: "))

def mintotal():
    total = print(f'{hora}h e {min}min somam ao todo {(hora * 60) + min}min')
    return total

mintotal()
