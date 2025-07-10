import random
import os
import utils as u

def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformadora(item)
        nova_colecao.append(item_transformado)

    return nova_colecao


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def reduzir(colecao, redutora, inicial):
    acumulado = inicial

    for item in colecao:
        acumulado = redutora(acumulado, item)

    return acumulado


def iniciar_playnumber(vetor):
    opcao_inicio = u.pedir_numero_faixa('\n>>> Opção: ', 1, 3)
    print('\n===========================================\n')

    if opcao_inicio == 1:
        tamanho_vetor = u.pedir_numero_positivo('Tamanho desejado para o vetor: ')
        limite_min = u.pedir_numero('Limite mínimo: ')
        limite_max = u.pedir_numero('Limite máximo: ')
        print()

        for _ in range(tamanho_vetor):
            numero = random.randint((limite_min), limite_max)
            vetor.append(numero)
        
    elif opcao_inicio == 2:
        tamanho_vetor = u.pedir_numero_positivo('Tamanho desejado para o vetor: ')
        limite_min = u.pedir_numero('Limite mínimo: ')
        limite_max = u.pedir_numero('Limite máximo: ')
        print()

        for i in range(tamanho_vetor):
            numero = u.pedir_numero_faixa(f'{i + 1}º valor: ', limite_min, limite_max)
            vetor.append(numero)

    elif opcao_inicio == 3:
        nome_arquivo = input('Informe o nome do arquivo: ')
        arquivo = open(nome_arquivo, 'r')

        for linha in arquivo:
            valor = linha.strip()
            vetor.append(int(valor))
        
    os.system('cls')


def mostrar_valores(lista):
    nova_lista = []
    
    for item in lista:
        nova_lista.append(item)

    print(nova_lista)


def resetar_vetor(lista):
    valor = u.pedir_numero('Resetar vetor pelo valor: ')
    
    for i in range(len(lista)):
        lista[i] = valor

    return lista


def ver_quantidade_itens(lista):
    return len(lista)


def menor_maior_valor_posicao(lista):
    maior = None
    posicao_maior = 0

    menor = None
    posicao_menor = 0

    for i in range(len(lista)):
        if maior == None or lista[i] > maior:
            maior = lista[i]
            posicao_maior = i + 1

        if menor == None or lista[i] < menor:
            menor = lista[i]
            posicao_menor = i + 1

    print(f'Menor Valor: {menor}\nPosição do menor: {posicao_menor}\n')
    print(f'Maior Valor: {maior}\nPosição do maior: {posicao_maior}')


def somatorio_valores(lista):
    somatorio = reduzir(lista, u.somar, 0)
    return somatorio


def media_valores(lista):
    media = somatorio_valores(lista) / len(lista)
    return media


def mostrar_positivos_quantidade(lista):
    positivos = filtrar(lista, lambda item:item > 0)
    mostrar_valores(positivos)
    
    print(f'\nQuantidade de positivos: {len(positivos)}')


def mostrar_negativos_quantidade(lista):
    negativos = filtrar(lista, lambda item:item < 0)
    mostrar_valores(negativos)

    print(f'\nQuantidade de negativos: {len(negativos)}')


def embaralhar(lista):
    nova_lista = []
    qtd_index = len(lista)

    for _ in range(len(lista)):
        valor_removido = lista.pop(random.randint(0, qtd_index - 1))
        nova_lista.append(valor_removido)
        qtd_index -= 1

    return nova_lista


def substituir_negativos(lista, minimo, maximo):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = random.randint(minimo, maximo)
        
    return lista


def adicionar_valores(lista):
    qtd_valores = u.pedir_numero_positivo('Quantidade de valores adicionados: ')

    for _ in range(qtd_valores):
        valor = u.pedir_numero('Valor a ser adicionado: ')
        lista.append(valor)

    return lista


def remover_valor_exato(lista):
    print(lista)
    valor_removido = u.pedir_numero('Qual valor da lista deseja remover? ')
    lista = filtrar(lista, lambda item:item != valor_removido)

    return lista


def remover_por_posicao(lista):
    print(lista)

    nova_lista = []
    posicao_removida = u.pedir_numero('Qual posição da lista deseja remover? ')

    for i in range(0, len(lista)):
        if i != posicao_removida - 1:
            nova_lista.append(lista[i])

    return nova_lista


def editar_valor_posicao(lista):
    print(lista)

    nova_lista = []
    posicao_removida = u.pedir_numero('Qual valor da lista deseja editar (pela posição)? ')
    valor = u.pedir_numero('Qual valor deseja adicionar na posição? ')

    for i in range(0, len(lista)):
        if i == posicao_removida - 1:
            nova_lista.append(i)
            lista[i] = valor

    return lista


def salvar_em_arquivo(lista):
    nome_arquivo = input('Digite o nome do arquivo: ')

    arquivo = open(nome_arquivo, 'w')
    linha = ''

    for item in lista:
        linha += f'{item}\n'

    arquivo.write(linha)