import utils

def main():
    n = utils.get_integer_number_min('Quantidade de termos: ', 1)
    utils.linhas()

    print('>>> SEQUÊNCIA DE FIBONACCI <<<')
    print(f'>>>>>>>> COM {n} TERMOS <<<<<<<<')
    definir_fibonacci(n)
    utils.linhas()

def definir_fibonacci(n: int):
   contador = 0
   valor1 = 0
   valor2 = 1

   while contador < n:
        print(valor1)
        sequencia = valor1 + valor2
        valor1 = valor2
        valor2 = sequencia
        contador += 1


main()