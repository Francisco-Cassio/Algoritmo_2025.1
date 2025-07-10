def main():
    soma = 0
    resultado = ''
    
    while True:
        m, n = map(int, input().split())

        if m <= 0 or n <= 0:
            break

        maior = m if m > n else n
        menor = n if n < m else m

        for i in range(menor, maior + 1, 1):
            soma += i
            resultado += str(f'{i} ')

        print(f'{resultado}Sum={soma}')
        
        soma = 0
        resultado = ''

    
main()