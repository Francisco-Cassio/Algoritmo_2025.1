def main():
    soma = 0
    qtd_positivos = 0

    for _ in range(0, 6, 1):
        valor = float(input())

        if valor > 0:
            qtd_positivos += 1
            soma += valor
            
    media = soma / qtd_positivos

    print(f'{qtd_positivos} valores positivos')
    print(f'{media:.1f}')


main()