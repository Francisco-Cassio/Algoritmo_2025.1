import utils

def main():
    tabuada = 1
    comeco = 1
    final = 10
    
    utils.linhas() 
    definir_tabuada(tabuada, comeco, final)


def definir_tabuada(tabuada: int, comeco: int, final: int):
    while comeco <= final:
        print(f'>>>>> TABUADA DO {comeco} <<<<<\n')
        while tabuada <= final:
            resultado = comeco * tabuada
            print(f'{comeco} x {tabuada} = {resultado}')
            
            tabuada += 1
        utils.linhas()    
        tabuada = 1
        comeco += 1


main()