# 13. Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
# descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
# somas. (Flag: salário=0)

# De            Até             Acréscimo
# R$ 0,00       R$ 2.999,99     25 %
# R$ 3.000,00   R$ 5.999,99     20 %
# R$ 6.000,00   R$ 9.999,99     15 %

# Acima de R$ 10.000,00 => 10 %

import utils


def main():
    soma_salarios = 0
    soma_novos_salarios = 0

    while True:
        salario = utils.get_decimal_number_min('Salário: R$ ', 0)
        utils.linhas()

        if salario == 0:
            break

        soma_salarios += salario

        if salario < 3000:
            salario += (salario * 0.25)
        elif salario < 6000:
            salario += (salario * 0.2)
        elif salario < 10000:
            salario += (salario * 0.15)
        else:
            salario += (salario * 0.1)

        soma_novos_salarios += salario

    diferenca = soma_novos_salarios - soma_salarios

    print(f'''Soma dos salários anteriores: R$ {soma_salarios:.2f}
Soma dos novos salários: R$ {soma_novos_salarios:.2f}
Diferença entre as somas: R$ {diferenca}''')
    utils.linhas()


main()