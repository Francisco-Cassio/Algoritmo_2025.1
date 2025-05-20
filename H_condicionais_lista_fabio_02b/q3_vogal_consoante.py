import utils

def main():
    letra = input('Digite uma letra: ').upper()
    utils.linhas()

    if letra in ('A', 'E', 'I', 'O', 'U'):
        print(f'{letra} é uma vogal')
    else:
        print(f'{letra} é uma consoante')


main()