from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num1 = obter_numero_inteiro('Primeiro Valor: ')
    num2 = obter_numero_inteiro('Segundo Valor: ')
    num3 = obter_numero_inteiro('Terceiro Valor: ')
    linhas()
    opcao = obter_numero_inteiro('Opção (1|2|3): ')

    escolha = escolha_valor(num1, num2, num3, opcao)

    linhas()

    if validar_opcao(opcao):
        print(f'O número escolhido foi: {escolha}')
    else:
        print('As opções são somente 1, 2 ou 3')


def validar_opcao(opcao: int):
    return 1 <= opcao <= 3


def escolha_valor(n1: int, n2: int, n3: int, opcao: int):
    if opcao == 1:
        return n1
    elif opcao == 2:
        return n2
    else:
        return n3
    

main()