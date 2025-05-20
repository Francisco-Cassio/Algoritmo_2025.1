from funcoes import obter_numero_real
from funcoes import linhas

def main():
    peso = obter_numero_real('Peso (kg): ')
    altura = obter_numero_real('Altura (m): ')

    linhas()

    if 10 <= altura < 100:
        altura = altura / 10
    elif altura >= 100:
        altura = altura / 100
    
    imc = calculo_imc(peso, altura)
    classificacao = classificacao_imc(imc)

    print(f'Seu IMC é: {imc:.1f}\nEstá classificado em: {classificacao}')


def calculo_imc(peso: float, altura: float):
    imc = peso / (altura**2)
    return imc


def classificacao_imc(imc: float):
    if imc < 25:
        return 'Peso Normal'
    elif imc <= 30:
        return 'Obeso'
    else:
        return 'Obesidade Mórbida'


main()