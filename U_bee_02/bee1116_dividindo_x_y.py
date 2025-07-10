def main():
    n = int(input())

    for _ in range(0, n, 1):
        x, y = map(int, input().split())

        try:
            result = x / y
            print(f'{result:.1f}')
        except ZeroDivisionError:
            print('divisao impossivel')


main()