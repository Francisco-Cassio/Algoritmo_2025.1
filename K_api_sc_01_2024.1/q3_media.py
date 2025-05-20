import utils
import os

def main():
    maior_nota = 0
    menor_nota = 0
    soma = 0

    qtd_alunos = 0

    qtd_homens = 0
    notas_homens = 0

    qtd_mulheres = 0
    notas_mulheres = 0

    utils.limpar_tela()
    while True:
        sexo = input('Sexo do Aluno (F/M): ')

        if sexo.upper() != 'M' and sexo.upper() != 'F':
            break

        nota = utils.get_decimal_number_min('Nota do Aluno: ', 1)
        utils.linhas()

        if qtd_alunos == 0:
            maior_nota = nota
            menor_nota = nota
        elif nota > maior_nota:
            maior_nota = nota
        elif nota < menor_nota:
            menor_nota = nota

        if sexo.upper() == 'M':
            qtd_homens += 1
            notas_homens += nota
        elif sexo.upper() == 'F':
            qtd_mulheres += 1
            notas_mulheres += nota

        soma += nota
        qtd_alunos += 1
    
    media = soma / qtd_alunos

    performance_homens = (notas_homens / soma) * 100
    performance_mulheres = (notas_mulheres / soma) * 100

    desempenho_alunos = calcular_desempenho(media)
    desempenho_homens = calcular_desempenho(performance_homens / 10)
    desempenho_mulheres = calcular_desempenho(performance_mulheres / 10)

    resultado = f'''
>>> RENDIMENTO DA TURMA <<<
------------------------------------
Maior Nota Geral: {maior_nota}
Menor Nota Geral: {menor_nota}
Média Geral da Turma: {media:.2f}
------------------------------------
=> PERFORMANCE:

> Homens: {performance_homens:.0f}%
> Mulheres: {performance_mulheres:.0f}%
------------------------------------
=> TOTAIS

> Alunos: {qtd_alunos}
> Homens: {qtd_homens}
> Mulheres: {qtd_mulheres}
------------------------------------
=> DESEMPENHO:

> Turma: {desempenho_alunos}
> Homens: {desempenho_homens}
> Mulheres: {desempenho_mulheres}
------------------------------------
'''
    utils.limpar_tela()
    print(resultado)


def calcular_desempenho(valor: float):
    if valor <= 2:
        return 'Péssimo'
    elif valor <= 4:
        return 'Ruim'
    elif valor <= 7:
        return 'Regular'
    elif valor <= 8:
        return 'Bom'
    else:
        return 'Excelente'
    

main()