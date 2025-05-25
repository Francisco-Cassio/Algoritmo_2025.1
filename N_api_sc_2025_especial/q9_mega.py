# 9. (q9_mega.py) Peça a um usuário um Prêmio da Mega-Sena o
# qual foi ganho por um grupo de Amigos. Em seguida, peça valores
# não-negativos que representam quanto cada amigo colaborou
# para comprar o bilhete premiado (ou bilhetes todos). Encerra
# quando for digitado zero. Sabemos que deve-se pagar 20% de
# Imposto sobre o prêmio, e então dividir o restante entre os
# amigos. O prêmio será dividido proporcionalmente, entretanto não
# precisa listar os prêmios individuais, apenas o Maior Prêmio
# Individual e o Menor Prêmio Individual.

# Ínicio às 11h29 em 25/05

from q1_number_utils import obter_numero_inteiro_positivo

def main():
    premio = obter_numero_inteiro_positivo('Prêmio da Mega-Sena: R$ ')

    soma = 0

    maior = None
    menor = None

    contador = 1
    while True:
        contribuicoes = obter_numero_inteiro_positivo(f'Colaboração do amigo {contador}: R$ ')

        if contribuicoes == 0:
            break
        
        if maior == None or contribuicoes > maior:
            maior = contribuicoes

        if menor == None or contribuicoes < menor:
            menor = contribuicoes

        soma += contribuicoes
        contador += 1

    premio_liquido = premio - (premio * 0.2)
    
    maior = (maior/soma) * premio_liquido
    menor = (menor/soma) * premio_liquido

    print(f'Maior Prêmio: R$ {maior:.2f}\nMenor Prêmio: R$ {menor:.2f}')


main()

# Finalziado às 11h46 em 25/05