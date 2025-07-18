import utils as u

def carregar_arquivo(nome_arquivo):
    escolas = []
    arquivo = open(nome_arquivo)

    for linha in arquivo:
        dados = linha.strip().split(';')
        escola = {}
        escola['ranking'] = dados[0]
        escola['nome'] = dados[1]
        escola['municipio'] = dados[2]
        escola['uf'] = dados[3]
        escola['rede'] = dados[4]
        escola['permanencia'] = dados[5]
        escola['nivel_socio_economico'] = dados[6]
        escola['media_objetivas'] = dados[7]
        escola['linguagens'] = dados[8]
        escola['matematica'] = dados[9]
        escola['ciencias_natureza'] = dados[10]
        escola['humanas'] = dados[11]
        escola['redacao'] = dados[12]

        escolas.append(escola)
    
    arquivo.close()
    return escolas


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def mapear(colecao, funcao):
    nova_colecao = []

    for item in colecao:
        novo_item = funcao(item)
        nova_colecao.append(novo_item)

    return nova_colecao


def reduzir(colecao, funcao, item_inicial):
    reduzido = item_inicial

    for item in colecao:
        reduzido = funcao(reduzido, item)

    return reduzido


def somatorio(colecao):
    somatorio = 0

    for item in colecao:
        somatorio += item

    return somatorio


def escolas_estado(escolas, estado):
    return filtrar(escolas, lambda escola: escola['uf'] == estado)


def topn_brasil(escolas, n):
    escolas_ordenadas = sorted(escolas, key=lambda x:float(x['media_objetivas'].replace(',', '.')), reverse=True)

    for i in range(min(n, len(escolas_ordenadas))):
        escola = escolas_ordenadas[i]
        print(f'{i+1}º - {escola['nome']}')


def validar_area(area):
    if area == 1:
        return 'linguagens'
    elif area == 2:
        return 'matematica'
    elif area == 3:
        return 'ciencias_natureza'
    elif area == 4:
        return 'humanas'
    elif area == 5:
        return 'redacao'
    else:
        print('Opção Inválida!')
        print()
        u.enter_continue()
        return


def obter_nome_area(nome_area):
    if nome_area == 'linguagens':
        print('>>> Área: Linguagens')
    elif nome_area == 'matematica':
        print('>>> Área: Matemática')
    elif nome_area == 'ciencias_natureza':
        print('>>> Área: Ciências da Natureza')
    elif nome_area == 'humanas':
        print('>>> Área: Humanas')
    elif nome_area == 'redacao':
        print('>>> Área: Redação')


def topn_brasil_area(escolas, area, n):
    try:
        nome_area = validar_area(area)        
        escolas_ordenadas = sorted(escolas, key=lambda x:float(x[nome_area].replace(',', '.')), reverse=True)
        obter_nome_area(nome_area)

        print()

        for i in range(min(n, len(escolas_ordenadas))):
            escola = escolas_ordenadas[i]
            print(f'{i+1}º - {escola['nome']} - Média: {escola[nome_area]}')
    except:
        print('Opção Inválida!')


def topn_estado(escolas, estado, n):
    print(f'>>> Estado: {estado.upper()}\n')
    return topn_brasil(escolas_estado(escolas, estado), n)


def top_estados_rede(escolas, estado, rede, n):
    print(f'>>> Estado: {estado.upper()} - Rede: {rede.title()}\n')
    return topn_brasil(filtrar(escolas_estado(escolas, estado), lambda escola: escola['rede'] == rede), n)


def media_nacional_area(escolas, area):
    nome_area = validar_area(area)

    escolas_filtradas = filtrar(escolas, lambda escola: escola[nome_area])
    escolas_filtradas = mapear(escolas_filtradas, lambda x: float(x[nome_area].replace(',', '.')))

    media = somatorio(escolas_filtradas) / len(escolas_filtradas)

    nome_area = obter_nome_area(nome_area)
    print()
    print(f'>>> Média: {media:.2f}')


def melhor_escola_area_estado(escolas, area, estado):
    print(f'>>> Estado: {estado.upper()}')
    topn_brasil_area(escolas_estado(escolas, estado), area, n=1)


def ordenar_estado_renda(escolas, estado):
    escolas_validas = filtrar(escolas_estado(escolas, estado), lambda escola: escola['nivel_socio_economico'] != 'Sem informação')
    escolas_ordenadas = sorted(escolas_validas, key= lambda x: x['nivel_socio_economico'], reverse= True)

    print(f'>>> Ordenado por Nível Socioeconômico - Estado: {estado.upper()}:\n')
    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        print(f'{i+1}º - {escola['nome']} - Nível Socioeconômico: {escola['nivel_socio_economico']}')


def menu_areas():
    menu = '''========== ÁREAS - ENEM 2014 ==========

1 - Linguagens
2 - Matematica
3 - Ciências da Natureza
4 - Humanas
5 - Redação

============================================

>>> Opção: '''

    return menu


def procurar_nome(escolas, parte_nome):
    nomes_escolas = []

    for escola in escolas:
        nomes_escolas.append(escola['nome'])

    escolas_filtradas = []

    print('>>> Busca por Nome:\n')
    for nome in nomes_escolas:
        if parte_nome in nome:
            escolas_filtradas.append(nome)
            print(f'{escolas_filtradas.index(nome) + 1}º - {nome}')


def ranking_enem_estado(escolas, estado):
    escolas_ordenadas = sorted(escolas_estado(escolas, estado), key=lambda x:float(x['ranking'].replace(',', '.')))

    print(f'>>> Estado: {estado.upper()}\n')
    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        print(f'{i+1}º - {escola['nome']} - Rank: {escola['ranking']}º')


def ranking_enem_regiao(escolas, estado, n):
    regioes = {
        'regiao_norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
        'regiao_nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
        'regiao_sudeste': ['ES', 'MG', 'RJ', 'SP'],
        'regiao_centroeste': ['GO', 'MT', 'MS', 'DF'],
        'regiao_sul': ['PR', 'SC', 'RS']
    }

    regiao_escolhida = ''

    for regiao, estados in regioes.items():
        if estado in estados:
            regiao_escolhida = regiao
            break

    if not regiao_escolhida:
        return ['Estado não encontrado']

    estados_regiao = regioes[regiao_escolhida]
    escolas_regiao = filtrar(escolas, lambda escola: escola['uf'] in estados_regiao)
    escolas_ordenadas = sorted(escolas_regiao, key= lambda x: float(x['media_objetivas'].replace(',', '.')), reverse=True)[:n]

    if regiao_escolhida == 'regiao_norte':
        nome_regiao = 'Norte'
    elif regiao_escolhida == 'regiao_nordeste':
        nome_regiao = 'Nordeste'
    elif regiao_escolhida == 'regiao_sudeste':
        nome_regiao = 'Sudeste'
    elif regiao_escolhida == 'regiao_centroeste':
        nome_regiao = 'Centro-Oeste'
    elif regiao_escolhida == 'regiao_sul':
        nome_regiao = 'Sul'

    print(f'>>> Região: {nome_regiao}\n')
    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        print(f'{i+1}º - {escola["nome"]} - Rank: {escola["ranking"]}º')