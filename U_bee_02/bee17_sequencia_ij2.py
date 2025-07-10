def main():
    I = 1
    J = 7

    while True:
        if I >= 10:
            break

        print(f'I={I} J={J}')

        J -= 1
        if J < 5:
            J = 7
            I += 2


main()