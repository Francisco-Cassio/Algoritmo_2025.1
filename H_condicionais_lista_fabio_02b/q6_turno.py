import utils

def main():
    turno = input('Turno do Aluno (M/V/N): ').upper()
    utils.linhas()

    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Valor Inválido!')


main()