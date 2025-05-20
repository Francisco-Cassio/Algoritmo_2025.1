def convert():
    num_meses = int(input("Informe o número de meses: "))
    num_anos = num_meses // 12
    new_num_meses = num_meses % 12
    print(f'{num_meses} mes(es) equivale a {num_anos} ano(s) e {new_num_meses} mes1(es)')

convert()