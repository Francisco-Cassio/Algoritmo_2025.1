def main():
    n = int(input())
    x = 1

    for _ in range(n):
        quadrado = x ** 2
        cubo = x ** 3
        print(f'{x} {quadrado} {cubo}')

        x += 1        


main()