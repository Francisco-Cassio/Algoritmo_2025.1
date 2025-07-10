def main():
    n = int(input())

    if n < 10000:
        for _ in range(n):
            x = int(input())

            if (-10**7) <= x <= (10**7):
                if x % 2 == 0 and x > 0:
                    print('EVEN POSITIVE')
                elif x % 2 != 0 and x > 0:
                    print('ODD POSITIVE')
                elif x % 2 == 0 and x < 0:
                    print('EVEN NEGATIVE')
                elif x % 2 != 0 and x < 0:
                    print('ODD NEGATIVE')
                elif x == 0:
                    print('NULL')


main()