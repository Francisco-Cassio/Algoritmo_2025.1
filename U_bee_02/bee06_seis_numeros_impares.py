def main():
    x = int(input())

    if x % 2 == 0:
        for i in range (x, x + 12, 1):
            if i % 2 != 0:
                print(i)
    else:
        for i in range (x, x + 11, 1):
            if i % 2 != 0:
                print(i)


main()