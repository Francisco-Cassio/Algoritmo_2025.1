from funcoes import obter_numero_real
from funcoes import linhas

def main():
    valor_quebrado = obter_numero_real('Valor decimal: ')

    linhas()

    valor = arrendondar(valor_quebrado)

    print(f'Arredonda-se {valor_quebrado} para {valor}')


def arrendondar(valor: float):
    if valor % 1 >= 0.5:
        return (valor + 1) // 1
    else:
        return valor // 1
    

main()