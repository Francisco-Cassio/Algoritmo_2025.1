def calculo():
    coeficiente_a = float(input("\nInforme o valor do coeficiente a: "))
    coeficiente_b = float(input("Informe o valor do coeficiente b: "))
    coeficiente_c = float(input("Informe o valor do coeficiente c: "))
    coeficiente_d = float(input("Informe o valor do coeficiente d: "))
    coeficiente_e = float(input("Informe o valor do coeficiente e: "))
    coeficiente_f = float(input("Informe o valor do coeficiente f: "))

    valor_x = (coeficiente_c*coeficiente_e - coeficiente_b*coeficiente_f) / (coeficiente_a*coeficiente_e) - (coeficiente_b*coeficiente_d)
    valor_y = (coeficiente_a*coeficiente_f) - (coeficiente_c*coeficiente_b) / (coeficiente_a*coeficiente_e) - (coeficiente_b*coeficiente_d)

    print(f'O sistema de equações lineares ax + by = c | dx + ey = f pode ser resolvido da seguinte forma:\nx = (ce - bf / ae - bd) e y = (af - cd/ae - bd)\nOnde:\nX = {valor_x:.1f}\nY = {valor_y:.1f}')

calculo()