# 2. (q2_numero_n.py) Dado um número inteiro N, e N sequências de
# números inteiros terminadas por 0, calcular e imprimir:
# a. A soma dos números pares de cada sequência.
# b. A média de todos os números digitados de todas as
# sequências.
# c. O menor e o maior números digitados de todas as sequências.


# ínicio às 20h19 em 24/05

from q1_number_utils import obter_numero_inteiro_min

def main():
    n = obter_numero_inteiro_min('Valor N de sequências: ', 1)
    print('-----------------------------------')

    contador = 1

    soma = 0
    soma_pares = 0
    total_numeros = 0

    maior = None
    menor = None

    while n > 0:
        print(f'Sequência N° {contador}:\n')
        while True:
            num = obter_numero_inteiro_min('Valor: ', 0)
            
            if num == 0:
                break
            
            soma += num
            total_numeros += 1

            if num % 2 == 0:
                soma_pares += num

            if maior == None or num > maior:
                maior = num

            if menor == None or num < menor:
                menor = num

        n -= 1
        
        print(f'''-----------------------------------
Soma dos números pares da {contador}° sequência: {soma_pares}
-----------------------------------''')
        contador +=1

        if n == 0:
            break
        
        soma_pares = 0
    
    media = soma / total_numeros

    print(f'''Média de todos os números digitados de todas as sequências: {media:.2f}
O menor número digitado de todas as sequências: {menor}
O maior número digitado de todas as sequências: {maior}''')
    

main()

# Finalizado às 20h56 em 24/05