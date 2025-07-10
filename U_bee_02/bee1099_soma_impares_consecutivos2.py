def main():
    n = int(input())
    for _ in range(n):
        n, y = map(int, input().split())
        print(soma_impares_entre(n, y))


def soma_impares_entre(n, y):
    if n > y:
        n, y = y, n

    soma = 0
    for i in range(n + 1, y):
        if i % 2 != 0:
            soma += i
    return soma


main()