def main():
    A, B, C = map(float, input().split())
    maior = A

    if B > A and B > C:
        maior = B
        if A > C:
            meio = A
            menor = C
        else:
            meio = C
            menor = A
    elif C > A and C > B:
        maior = C
        if A > B:
            meio = A
            menor = B
        else:
            meio = B
            menor = A
    else:
        if B > C:
            meio = B
            menor = C
        else:
            meio = C
            menor = B

    if A > 0 and B > 0 and C > 0:
        if maior >= (meio + menor):
            print('NAO FORMA TRIANGULO')
        elif (maior ** 2) == (meio ** 2 + menor ** 2):
            print('TRIANGULO RETANGULO')
        elif (maior ** 2) > (meio ** 2 + menor ** 2):
            print('TRIANGULO OBTUSANGULO')
        else:
            print('TRIANGULO ACUTANGULO')
        
        if A == B == C:
            print('TRIANGULO EQUILATERO')
        elif A == B or B == C or C == A:
            print('TRIANGULO ISOSCELES')


main()