def main():
    num_pares = 0
    num_impares = 0
    num_positivos = 0
    num_negativos = 0

    for _ in range(0, 5, 1):
        valor = int(input())

        if valor % 2 == 0:
            num_pares += 1
        else:
            num_impares += 1
        
        if valor > 0:
            num_positivos += 1
        elif valor < 0:
            num_negativos += 1
    
    print(f'{num_pares} valor(es) par(es)')
    print(f'{num_impares} valor(es) ímpar(es)')
    print(f'{num_positivos} valor(es) positivo(s)')
    print(f'{num_negativos} valor(es) negativo(s)')


main()