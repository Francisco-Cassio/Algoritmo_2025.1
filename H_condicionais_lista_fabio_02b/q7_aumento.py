import utils

def main():
    salario = utils.get_decimal_number_min('Salário: R$ ', 0)
    utils.linhas()

    salario_novo = 0
    porcentagem = 0

    if salario <= 280:
        salario_novo = aumento(salario, 0.2)
        porcentagem = 20

    elif salario <= 700:
        salario_novo = aumento(salario, 0.15)
        porcentagem = 15
        
    elif salario <= 1500:
        salario_novo = aumento(salario, 0.1)
        porcentagem = 10

    else:
        salario_novo = aumento(salario, 0.05)
        porcentagem = 5

    valor_aumento = salario * (porcentagem / 100)

    resultado = f'''Salário antes do reajuste: {salario:.2f}
Percentual de aumento aplicado: {porcentagem}%
Valor do aumento: R$ {valor_aumento:.2f}
Novo salário, após o aumento: R$ {salario_novo:.2f}'''
    
    print(resultado)


def aumento(salario: float, porcentagem: float):
    return (salario * porcentagem) + salario

main()