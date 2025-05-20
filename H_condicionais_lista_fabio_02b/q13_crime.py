import utils

def main():
    suspeitas = 0

    print('Reponda com S para sim e N para não!')
    utils.linhas()

    q1 = input('Telefonou para a vítima? ').upper()
    if q1 == 'S':
        suspeitas += 1

    q2 = input('Esteve no local do crime? ').upper()
    if q2 == 'S':
        suspeitas += 1

    q3 = input('Mora perto da vítima? ').upper()
    if q3 == 'S':
        suspeitas += 1

    q4 = input('Devia para a vítima? ').upper()
    if q4 == 'S':
        suspeitas += 1

    q5 = input('Já trabalhou com a vítima? ').upper()
    if q5 == 'S':
        suspeitas += 1

    utils.linhas()

    if suspeitas == 2:
        print('Situação: Suspeita!')
    elif suspeitas == 3 or suspeitas == 4:
        print('Situação: Cúmplice!')
    elif suspeitas == 5:
        print('Situação: Assassino!')
    else:
        print('Situação: Inocente!')


main()