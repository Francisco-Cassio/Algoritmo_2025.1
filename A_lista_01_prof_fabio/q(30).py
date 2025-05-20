def convert():
    num_min = int(input("Informe os minutos: "))
    #1h = 60min / 1d = 24*60 = 1440
    num_dias = num_min // 1440
    num_horas = (num_min % 1440) // 60
    new_num_min = num_min % 60
    print(f'{num_min}min equivale a {num_dias:.0f}d {num_horas:.0f}h e {new_num_min:.0f}min')

convert()