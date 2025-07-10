def main():
    lanche, qtd = map(int, input().split())

    total = 0

    if lanche == 1:
        total =  4 * qtd
    elif lanche == 2:
        total = 4.5 * qtd
    elif lanche == 3:
        total = 5 * qtd
    elif lanche  == 4:
        total = 2 * qtd
    elif lanche == 5:
        total = 1.5 * qtd

    print(f'Total: R$ {total:.2f}')


main()