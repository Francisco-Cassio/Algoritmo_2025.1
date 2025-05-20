# O aumento ou perda de peso, de forma simplificada, é um o resultado da balança entre superávit ou déficit calórico. Se consumir mais do que precisa, aumenta o peso, caso contrário diminui ou mantém. 
# De acordo com a OMS, um homem adulto em média precisa consumir apenas 2400 calorias/dia para manter o peso atual. Já as mulheres ficam em 2000 calorias. Ou seja, esse é o valor que gastamos em atividades do dia a dia, normais. Já para perder 1kg de peso é necessário o gasto calórico excedente de 7000 calorias. 
# Na academia, temos uma série de exercícios do tipo aeróbico, dentre eles o Transport e Simulador de Escada. No Transport, um homem gasta em média 100 calorias a cada 5 min, já uma mulher a cada 6 min. E na escada, um homem gasta 100 calorias a cada 7 minutos e a mulher a cada 8 minutos. 
# Considerando as informações acima como verdade (informações hipotéticas), e que o ritmo alimentar permanecerá o mesmo. 
# Faça um programa para auxiliar na perda de peso de homens e mulheres adultos. O objetivo é, de acordo com a situação atual (peso atual, se homem ou mulher, quantos quilos quer perder, quantos dias por semana irá fazer atividade física, e quanto tempo por dia irá treinar). Pergunte ainda qual proporção (%) de tempo alocada para o Transport, e calcule a contrapartida de Escada (os dois serão 100%). 
# Seu objetivo, ao final, é informar em quantas semanas o usuário alcançará o objeto desejado, bem como indicar para cada dia de atividade física, quantos minutos de escada e quantos de Transport ele deverá seguir (todos os dias são iguais). Faça as validações adequadas. 

import utils

def main():
    peso_atual = utils.get_decimal_number_min('Peso Atual: ', 1)
    sexo = input('Sexo (H/M): ')
    meta_perda = utils.get_decimal_number_min('Quantos quilos quer perder? ', 1)
    dias_atividade = utils.get_integer_number_min('Quantos dias por semana irá fazer atividade física? ', 1)
    tempo_dia = utils.get_integer_number_min('Quanto tempo por dia irá treinar (min)? ', 1)

    tempo_transport = utils.get_integer_number_min('Deste tempo, quanto será dedicado ao Transport? ', 1)
    tempo_escadas = tempo_dia - tempo_transport

    meta_peso = peso_atual - meta_perda
    days = dias_atividade
    dias = 1

    calorias_perdidas_homens = 0
    calorias_perdidas_mulheres = 0

    while peso_atual >= meta_peso:
        while dias_atividade >= 0:

            if sexo.upper() == 'H':

                while tempo_transport >= 0:
                    calorias_perdidas_homens += 100
                    tempo_transport -= 5
                
                while tempo_escadas >= 0:
                    calorias_perdidas_homens += 100
                    tempo_escadas -= 7

            elif sexo.upper() == 'M':

                while tempo_transport >= 0:
                    calorias_perdidas_mulheres += 100
                    tempo_transport -= 6
                
                while tempo_escadas >= 0:
                    calorias_perdidas_mulheres += 100
                    tempo_escadas -= 8
            
            dias_atividade -= 1
        
        dias_atividade += days

        if calorias_perdidas_homens == 7000:
            peso_atual -= 1
            calorias_perdidas_homens = 0

        elif calorias_perdidas_mulheres == 7000:
            peso_atual -= 1
            calorias_perdidas_mulheres = 0

        dias += 1
            
    semanas = dias / 7

    print(semanas)

main()