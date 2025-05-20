def convert():
    num_segundos = int(input("Informe um número de segundos: "))
    num_horas = num_segundos // 3600
    num_min = (num_segundos % 3600) / 60
    new_num_segundos = (num_segundos % 3600) % 60
    print(f'{num_segundos}s equivale a {num_horas}h {num_min:.0f}min e {new_num_segundos:.0f}s')

convert()