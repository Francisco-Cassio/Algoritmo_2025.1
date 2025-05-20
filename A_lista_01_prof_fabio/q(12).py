def aumento():
    salario = float(input("\nInforme o salário(R$): "))
    aumento_percentual = salario * 0.25
    salario_total = salario + aumento_percentual
    print(f'O salário de R${salario:.2f} será R${salario_total:.2f} após o aumento de 25%')

aumento()