import utils

def main():
    qtd_funcionarios = utils.get_integer_number_min('Quantidade de funcionário: ', 1)
    utils.linhas()

    print('\n>>> FICHA DOS TRABALHADORES <<<')
    utils.linhas()
    ler_ficha(qtd_funcionarios)


def ler_ficha(n: int):
    contador = 1

    while contador <= n:
        codigo = utils.get_integer_number_min('\nCódigo do funcionário: ', 1)
        horas = utils.get_integer_number_min('Número de horas trabalhadas: ', 1)
        n_dependentes = utils.get_integer_number_min('Número de dependentes: ', 0)
        utils.linhas()

        salario = horas_trabalho(horas) + dependentes(n_dependentes)
        valor_inss = inss(salario)
        valor_ir = ir(salario)
        sal_descontado = salario - (valor_inss + valor_ir)

        print(f'\n>>> FUNCIONÁRIO {contador}:')
        utils.linhas()
        print(f'>>> CÓDIGO: {codigo}\n>>> HORAS TRABALHADAS: {horas}\n>>> N° DE DEPENDENTES: {n_dependentes}')
        utils.linhas()
        print(f'>>> Valor descontado para o INSS: R$ {valor_inss:.2f}\n>>> Valor descontado para o IR: R$ {valor_ir:.2f}\n>>> Salário Líquido: R$ {sal_descontado:.2f}')
        utils.linhas()

        contador += 1

def horas_trabalho(h: int):
    return h * 12


def dependentes(d: int):
    return d * 40


def inss(sal: float):
    return sal * 0.085


def ir(sal: float):
    return sal * 0.05


main()