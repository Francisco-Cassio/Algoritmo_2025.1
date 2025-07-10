def main():
    soma = 0

    for _ in range(2):
        while True:
            nota = float(input())

            if 0 <= nota <= 10:
                soma += nota
                break
            else:
                print('nota invalida')
    
    media = soma / 2

    print(f'media = {media:.2f}')


main()