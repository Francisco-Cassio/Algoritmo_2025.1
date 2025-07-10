def main():
    num_pares = 0
    
    for _ in range(0, 5, 1):
        valor = int(input())

        if valor % 2 == 0:
            num_pares += 1

        
    print(f'{num_pares} valores pares')


main()