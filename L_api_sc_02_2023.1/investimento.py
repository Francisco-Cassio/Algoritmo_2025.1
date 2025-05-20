import utils

def main():
    objetivo = input('Qual o objetivo? ')
    valor_necessario = utils.get_decimal_number_min('Quanto precisa para realizá-lo? R$ ', 1)
    salario = utils.get_decimal_number_min('Salário: R$ ', 1)
    investimento = utils.get_integer_number_min('Porcentagem para investir mensalmente: ', 1)/100
    taxa_juros = utils.get_decimal_number_min('Taxa de juros do investimento: ', 1)

    definir_investimento(objetivo, valor_necessario, salario, investimento, taxa_juros)


def definir_investimento(objetivo: str, valor_necessario: float, salario: float, investimento: int, taxa_juros: float):

    if investimento > 0.3:
        utils.linhas()
        print('\nO valor do investimento deve ser no máximo de 30%')
        utils.linhas()
        investimento = utils.get_integer_number_min('Porcentagem para investir mensalmente: ', 1)/100
        return definir_investimento(objetivo, valor_necessario, salario, investimento, taxa_juros)

    elif taxa_juros > 1:
        utils.linhas()
        print('\nO valor do investimento deve ser no máximo de 1%')
        utils.linhas()
        taxa_juros = utils.get_decimal_number_min('Taxa de juros do investimento: ', 1)
        return definir_investimento(objetivo, valor_necessario, salario, investimento, taxa_juros)
    
    else:
    
        ano = 0
        mes = 0

        investimento_com_juros = 0

        while investimento_com_juros <= valor_necessario:
            valor_para_investimento = salario * investimento
            investimento_com_juros += ((valor_para_investimento * taxa_juros) + valor_para_investimento)

            mes += 1

        utils.limpar_tela()
        resultado = f'''>>>>> MARIANA INVESTIMENTO'S <<<<<
-----------------------------------
Objetivo: {objetivo}
Valor necessário: R$ {valor_necessario:.2f}
-----------------------------------
Salário: R$ {salario:.2f}
Porcentagem para investir: {(investimento * 100):.0f}% por mês
Taxa de juros: {taxa_juros}%
-----------------------------------

=> CONCLUSÃO
'''
        print(resultado)
        calcular_tempo(ano, mes)
        utils.linhas()


def calcular_tempo(ano: int, mes: int):
    if mes == 12:
        print(f'O objetivo foi alcançado em 1 ano')

    elif mes >= 12:
        while mes >= 12:
            ano += 1
            mes -= 12
        print(f'O objetivo foi alcançado em {ano} ano(s) e {mes} mes(es)')

    else:
        print(f'O objetivo foi alcançado em {mes} mes(es)')


main()