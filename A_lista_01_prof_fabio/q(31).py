def binario_to_decimal():
    num_binario = int(input("\nDigite um número binário de 4 dígitos(0/1): "))
    #a ordem de separação dos bits vai ser da esquerda para a diteira(-->)
    primeiro_bit = num_binario // 1000
    segundo_bit = (num_binario % 1000) // 100
    terceiro_bit = ((num_binario % 1000) % 100) // 10
    quarto_bit = ((num_binario % 1000) % 100) % 10

    new_primeiro_bit = primeiro_bit * 2**3
    new_segundo_bit = segundo_bit * 2**2
    new_terceiro_bit = terceiro_bit * 2**1
    new_quarto_bit = quarto_bit * 2**0
    print(f'{primeiro_bit}{segundo_bit}{terceiro_bit}{quarto_bit} na base binária equivale a {new_primeiro_bit + new_segundo_bit + new_terceiro_bit + new_quarto_bit} na base decimal')

binario_to_decimal()