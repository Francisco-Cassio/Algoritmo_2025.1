import utils

def main():
    sexo = input('Qual seu sexo (F/M)? ')
    utils.linhas()
    
    if sexo.upper() == 'F':
        print('Feminino')
    elif sexo.upper() == 'M':
        print('Masculino')
    else:
        print('Sexo Inválido')


main()