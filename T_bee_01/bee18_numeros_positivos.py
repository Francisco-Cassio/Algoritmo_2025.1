def main():
    num_positivos = 0

    for _ in range(0, 6, 1):
        valor = float(input())

        if valor > 0:
            num_positivos += 1
    
    print(f'{num_positivos} valores positivos')


main()