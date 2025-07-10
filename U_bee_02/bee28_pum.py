def main():
    n = int(input())
    x, y, z = 1, 2, 3

    for _ in range(n):
        print(x, y, z, 'PUM')
        x += 4
        y += 4
        z += 4


main()