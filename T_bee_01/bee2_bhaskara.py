def main():
    A, B, C = map(float, input().split())

    delta = calcular_delta(A, B, C)

    if delta < 0 or A == 0:
        print('Impossivel calcular')
    else:
        R1 = (-B + (delta ** (1/2))) / (2 * A)
        R2 = (-B - (delta ** (1/2))) / (2 * A)

        print(f'R1 = {R1:.5f}')
        print(f'R2 = {R2:.5f}')


def calcular_delta(A: float, B: float, C: float):
    return (B ** 2) - (4 * A * C)


main()