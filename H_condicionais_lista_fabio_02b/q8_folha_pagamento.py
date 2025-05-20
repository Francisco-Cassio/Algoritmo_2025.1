import utils

def main():
    valor = utils.get_decimal_number_min('Valor pela hora: R$ ', 0)
    hora = utils.get_integer_number_min('Quantas horas? ', 0)
    utils.linhas()
    
    salario_bruto = hora * valor
    
    descontos = 0
    porcentagem = 0

    if salario_bruto > 900 and salario_bruto <= 1500:
        ir = imposto_renda(salario_bruto, 0.05)
        porcentagem = 5
        descontos += ir

    elif salario_bruto <= 2500:     
        ir = imposto_renda(salario_bruto, 0.1)
        porcentagem = 10
        descontos += ir

    elif salario_bruto > 2500:     
        ir = imposto_renda(salario_bruto, 0.2)
        porcentagem = 20
        descontos += ir

    sindicato = salario_bruto * 0.03
    inss = salario_bruto * 0.1

    descontos += inss

    fgts = salario_bruto * 0.11

    salario_novo = salario_bruto - descontos

    resultado = f'''Salário Bruto:\t\tR$ {salario_bruto:.2f}
(-) IR ({porcentagem}%) :\t\tR$ {ir:.2f}
(-) INSS (10%) :\tR$ {inss:.2f}
FGTS (11%) :\t\tR$ {fgts:.2f}
Total de descontos :\tR$ {descontos:.2f}
Salário Liquido :\tR$ {salario_novo:.2f}'''

    print(resultado)
    utils.linhas()
    
def imposto_renda(bruto: float, porcentagem: float):
    return bruto * porcentagem


main()