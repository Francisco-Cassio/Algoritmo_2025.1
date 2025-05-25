# 7. (q7_habilidades.py) Murilo acabou de iniciar seu curso de
# graduação na faculdade de ADS e precisa de sua ajuda para
# organizar dados estatísticos com os veteranos. Ela gostaria de
# saber quantos alunos têm desejo aptidão em quatro áreas
# “tradicionais” do desenvolvimento.

# São elas: Frontend, Mobile, Backend e Dados. Para obter estas
# informações, ela sabe exatamente quantos alunos vai questionar
# previamente, o tipo de habilidade/área e as quantidades detalhadas.
# Ele agrupou a pesquisa em blocos, por exemplo abaixo

# Exemplo de Entrada        Exemplo de Saída

# 10                        Total: 92 alunos
# 10 B                      Total de Backend: 29
# 6 F                       Total de Frontend: 40
# 15 M                      Total de Mobile: 23
# 5 B                       Total de Dados: 0
# 14 F                      Percentual de Backend: 31.52 %
# 9 B                       Percentual de Frontend: 43.48 %
# 6 F                       Percentual de Mobile: 25.00 %
# 8 M                       Percentual de Dados: 0.00 %
# 5 B
# 14 F

# OBS.: Como receber dados na mesma linha
# entrada = "10 B"
# n = int(entrada.split()[0])
# tipo = entrada.split()[1]

# 24-05/23h45- 24-05/00h11

from q1_number_utils import obter_numero_inteiro_min


def main():
    total_alunos = 0
    total_back = 0
    total_front = 0
    total_mobile = 0
    total_dados = 0

    quantidade = obter_numero_inteiro_min('', 1)

    validar_entrada(quantidade, total_alunos, total_back, total_front, total_mobile, total_dados)
        


def validar_entrada(quantidade: int, total_alunos: int, total_back: int, total_front: int, total_mobile: int, total_dados: int):
    while quantidade > 0:
        entrada = input()
        n = int(entrada.split()[0])
        tipo = (entrada.split()[1]).upper()

        if tipo == 'B':
            total_back += n
        elif tipo == 'F':
            total_front += n
        elif tipo == 'M':
            total_mobile += n
        elif tipo == 'D':
            total_dados += n
        else:
            print('Opção inválida! Tente novamente...')
            return validar_entrada(quantidade, total_alunos, total_back, total_front, total_mobile, total_dados)
        
        total_alunos += n
        quantidade -= 1
        
    percentual_back = (total_back / total_alunos) * 100
    percentual_front = (total_front / total_alunos) * 100
    percentual_mobile = (total_mobile / total_alunos) * 100
    percentual_dados = (total_dados / total_alunos) * 100

    print(f'''-----------------------------------
Total: {total_alunos} alunos
Total de Backend: {total_back}
Total de Frontend: {total_front}
Total de Mobile: {total_mobile}
Total de Dados: {total_dados}
Percentual de Backend: {percentual_back:.2f} %
Percentual de Frontend: {percentual_front:.2f} %
Percentual de Mobile: {percentual_mobile:.2f} %
Percentual de Dados: {percentual_dados:.2f} %''')


main()