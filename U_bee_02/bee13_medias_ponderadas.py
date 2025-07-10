def main():
    n = int(input())

    for _ in range(0, n, 1):
        valor1, valor2, valor3 = map(float, input().split())
        media = ((valor1 * 2) + (valor2 * 3) + (valor3 * 5)) / 10
        print(f'{media:.1f}')


main()