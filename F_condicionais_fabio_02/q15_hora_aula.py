from funcoes import obter_numero_inteiro
from funcoes import obter_numero_real
from funcoes import linhas

def main():
    horas_aula1 = obter_numero_inteiro('Quantidade de horas aula do Professor 01: ')
    valor_hora01 = obter_numero_real('Valor por hora do Professor 01: ')
    linhas()
    horas_aula2 = obter_numero_inteiro('Quantidade de horas aula do Professor 02: ')
    valor_hora02 = obter_numero_real('Valor por hora do Professor 02: ')

    salario_um = definir_salario(horas_aula1, valor_hora01)
    salario_dois = definir_salario(horas_aula2, valor_hora02)

    linhas()

    if salario_maior(horas_aula1, valor_hora01, horas_aula2, valor_hora02):
        print(f'Salário do Professor 01: R$ {salario_um} -> (MAIOR SALÁRIO)\nSalário do Professor 02: R$ {salario_dois}')
    else:
        print(f'Salário do Professor 01: R$ {salario_um}\nSalário do Professor 02: R$ {salario_dois} -> (MAIOR SALÁRIO)')


def definir_salario(hora: int, valor: float):
    return (f'{((valor * hora) * 23):.2f}')


def salario_maior(hora_um: int, valor_um: float, hora_dois: int, valor_dois: float):
    return definir_salario(hora_um, valor_um) > definir_salario(hora_dois, valor_dois)


main()