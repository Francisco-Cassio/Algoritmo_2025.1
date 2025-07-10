def main():
    I = 1
    J = 7
    new_J = J

    while True:
        if I >= 10:
            break

        print(f'I={I} J={J}')

        J -= 1
        if J < (new_J - 2):
            J = new_J + 2
            new_J = J
            I += 2


main()