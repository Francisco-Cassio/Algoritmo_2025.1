from funcoes import obter_numero_real
from funcoes import linhas

def main():
    nota1 = obter_numero_real('Primeira Nota: ')
    nota2 = obter_numero_real('Segunda nota: ')

    linhas()

    situacao(nota1, nota2)


def obter_media(n1: float, n2: float):
    return (n1 + n2) / 2


def situacao(n1: float, n2: float):
    media = obter_media(n1, n2)
    if media >= 7:
        print('Aprovado')
    else:
        exame = obter_numero_real('Nota do Exame: ')    
        nova_media = (exame + media) / 2

        linhas()
        
        if nova_media >= 5:
            print('Aprovado')
        else:
            print('Reprovado')


main()