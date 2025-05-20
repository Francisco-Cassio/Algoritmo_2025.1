def convert():
    num_dias = int(input("\nInforme um número de dias: "))
    valor_semana = num_dias // 7
    new_num_dias = num_dias % 7
    print(f'{num_dias} dia(s) equivale a {valor_semana} semana(s) e {new_num_dias} dia(s)')

convert()