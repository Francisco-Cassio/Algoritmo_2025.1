# 10. Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
# pode levantar vôo ou não. Considere os seguintes critérios:
# · O peso de decolagem da aeronave é sempre igual a 500.000 kg;
# · O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
# passageiros;
# · O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
# · A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
# · O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
# · O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
# bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
# estimado de 10kg.
# O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
# ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
# bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
# de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
# mensagem indicando a liberação da decolagem ou não.

import utils

def main():
    n_containers = utils.get_integer_number_min('N° de containers: ', 1)
    utils.linhas()

    peso_decolagem = 500000
    peso_total = 0

    peso_carga = 0
    peso_passageiro = 0
    peso_bagagens = 0
    
    contador = 1
    while n_containers > 0:
        peso_container = utils.get_integer_number_min(f'Peso do {contador}° container: ', 1)

        peso_carga += peso_container
        contador += 1
        n_containers -= 1


    qtd_passageiros = 0
    contador = 1

    while True:
        utils.linhas()
        n_bilhete = utils.get_integer_number_min('N° bilhete: ', 0)
        
        if n_bilhete == 0:
            break

        qtd_bagagens = utils.get_integer_number_min('Quantidade de bagagens: ', 1)

        peso_passageiro += 70
        qtd_passageiros += 1
        
        while qtd_bagagens > 0:
            peso_bagagens += 10
        
            qtd_bagagens -= 1

    peso_total = peso_passageiro + peso_carga
    peso_decolagem -= peso_total

    quantidade_combustivel = peso_decolagem / 1.5
    
    total = peso_bagagens + peso_passageiro + peso_carga + peso_decolagem

    resultado = f'''>>>>> AVALIAÇÃO DA CARGA <<<<<
-----------------------------------
Quantidade de passageiro: {qtd_passageiros}

Volume total de bagagens: {peso_bagagens}
Peso dos passageiros: {peso_passageiro}
Peso das cargas: {peso_carga}

Quantidade possível de combustível: {quantidade_combustivel:.1f}L
-----------------------------------'''
    
    utils.limpar_tela()
    print(resultado)

    if total == 500000:
        print(f'=> Liberado para decolagem!')
    else:
        print(f'=> Decolagem não liberada!')
    
    utils.linhas()


main()