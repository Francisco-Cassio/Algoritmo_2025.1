import os

def limpar_tela():
    os.system('cls')


def enter_to_continue():
    print('===========================================\n')
    input('Aperter <Enter> para continuar...')
    limpar_tela()


def inicio():
    menu = '''
=============== PlayNumbers ===============

>>> Olá, bem-vindo ao PlayNumbers!

>>> Você deseja:

1 - Inicializar um vetor com dados automáticos
2 - Informar os dados do vetor
3 - Inicializar com dados de um arquivo

==========================================='''

    print(menu)


def inicio_realizado():
    operacao_realizada = '''
=============== PlayNumbers ===============

>>> Vetor inicializado com sucesso!!!
'''
    print(operacao_realizada)


def menu_principal():
    menu = '''
=============== PlayNumbers ===============

1 - Mostrar todos os valores
2 - Resetar Vetor
3 - Ver quantidade de itens no vetor
4 - Ver Menor e Maior valores e suas posições
5 - Somatório dos Valores
6 - Média dos Valores
7 - Mostrar Valores Positivos e Quantidade
8 - Mostrar Valores Negativos e Suas Quantidades
9 - Atualizar todos os valores por uma das regras:
10 - Adicionar Novos Valores
11 - Remover Itens por Valor exato
12 - Remover por Posição
13 - Editar valor específico por Posição
14 - Salvar valores em arquivo
15 - Sair

==========================================='''

    print(menu)


def regras():
    regras = '''
=============== Regras ===============

1 - Multiplicar por um valor
2 - Elevar a um valor (exponenciação)
3 - Reduzir a uma fração (Pedir a fração - Ex: ⅕)
4 - Substituir valores negativos por um número aleatório de uma faixa (min, max)
5 - Ordenar valores (Cescente, Decrescente)
6 - Embaralhar valores

======================================'''

    print(regras)
    

def ordenacao():
    ordem = '''
=============== Ordenação ===============

Ordenar a vetor em ordem:

1 - Crescente
2 - Decrescente

========================================='''

    print(ordem)


def pedir_numero(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print('O valor deve ser um número! Tente novamente...\n')
        return pedir_numero(label)
    

def pedir_numero_positivo(label):
    numero = pedir_numero(label)

    if numero > 0:
        return numero
    else:
        print('O valor deve ser positivo! Tente novamente...\n')
        return pedir_numero_positivo(label)
    

def pedir_numero_negativo(label):
    numero = pedir_numero(label)

    if numero < 0:
        return numero
    else:
        print('O valor deve ser negativo! Tente novamente...\n')
        return pedir_numero_negativo(label)
    

def pedir_numero_faixa(label, min, max):
    numero = pedir_numero(label)

    if min <= numero <= max:
        return numero
    else:
        print(f'O valor deve estar entre {min} e {max}! Tente novamente...\n')
        return pedir_numero_faixa(label, min, max)
    

def somar(valor1, valor2):
  return valor1 + valor2