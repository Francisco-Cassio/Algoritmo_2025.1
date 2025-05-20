def convert():
    num_horas = int(input("Informe o número de horas(h): "))
    # 1 dia = 24h/ 1 semana = 24 * 7 = 168h
    num_semana = num_horas // 168
    num_dias = (num_horas % 168) // 24
    new_num_horas = (num_horas % 24)
    print(f'{num_horas}h equivale a {num_semana:.0f} semana(s) {num_dias:.0f}d e {new_num_horas:.0f}h')

convert()