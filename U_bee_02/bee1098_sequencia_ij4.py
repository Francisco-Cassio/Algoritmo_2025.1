def main():
    i = 0
    while i <= 20:
        j = 1
        while j <= 3:
            I = i / 10
            J = j + I

            if i % 10 == 0:
                print(f'I={int(I)} J={int(J)}')
            else:
                print(f'I={I:.1f} J={J:.1f}')
            j += 1
        i += 2

main()
