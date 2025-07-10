def main():
    n = int(input())

    if 2 <= n <= 1000:
        for i in range(1, 11, 1):
            print(f'{i} x {n} = {n * i}')


main()