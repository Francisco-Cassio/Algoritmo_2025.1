def main():
    salario = float(input())
    imposto = 0

    if salario <= 2000:
        print("Isento")
    else:
        resto_salario = salario

        if salario > 4500:
            imposto += (salario - 4500) * 0.28
            resto_salario = 4500

        if salario > 3000.00:
            imposto += (resto_salario - 3000) * 0.18
            resto_salario = 3000

        if salario > 2000:
            imposto += (resto_salario - 2000) * 0.08

        print(f"R$ {imposto:.2f}")

main()