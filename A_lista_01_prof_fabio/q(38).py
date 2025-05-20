
def soma_fracoes():
    numerador_1 = float(input("Informe o numerador da 1º fração: "))
    denominador_1 = float(input("Informe o denominador da 1º fração: "))
    numerador_2 = float(input("Informe o numerador da 2º fração: "))
    denominador_2 = float(input("Informe o denomindador da 2º fração: "))

    soma_numerador = (numerador_1*denominador_2 + numerador_2*denominador_2) 
    soma_denominador = denominador_1 * denominador_2
    
    print(f'A soma de {numerador_1}/{denominador_1} por {numerador_2}/{denominador_2} é igual a {soma_numerador:.1f}/{soma_denominador:.1f}')

soma_fracoes()