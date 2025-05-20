def calculo_media_ponderada():
    nota1 = float(input("Informe a 1º nota: "))
    peso1 = float(input("Informe o peso da 1ª nota: "))

    nota2 = float(input("Informe a 2º nota: "))
    peso2 = float(input("Informe o peso da 2ª nota: "))

    nota3 = float(input("Informe a 3º nota: "))
    peso3 = float(input("Informe o peso da 3ª nota: "))

    media_ponderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)
    print(f'A média ponderada do aluno é: {media_ponderada:.2f}')

calculo_media_ponderada()