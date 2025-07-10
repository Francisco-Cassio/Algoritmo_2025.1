def main():
    maior = None
    posicao = 0

    for i in range(1, 101):
        num = int(input())

        if maior == None or num > maior:
            maior = num
            posicao = i

    print(maior)
    print(posicao)


main()