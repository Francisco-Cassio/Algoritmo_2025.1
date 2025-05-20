# 11. Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por
# matrícula = 0. Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula:

# Média Final = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10

# Se a média final for igual ou superior a 7, o aluno está aprovado; se a média final for inferior a 7, o
# aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total
# de alunos da turma.

import utils

def main():
    alunos_aprovados = 0
    alunos_reprovados = 0

    while True:
        matricula = utils.get_integer_number_min('N° da matrícula: ', 0)

        if matricula == 0:
            break

        utils.linhas()
        nota1 = utils.get_decimal_number_min('Nota 1: ', 0)
        nota2 = utils.get_decimal_number_min('Nota 2: ', 0)
        nota3 = utils.get_decimal_number_min('Nota 3: ', 0)
        utils.linhas()

        media = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10

        if media >= 7:
            alunos_aprovados += 1
            print('Aluno aprovado!')
        else:
            alunos_reprovados += 1
            print('Aluno reprovado!')
        
        utils.linhas()

    total_alunos = alunos_aprovados + alunos_reprovados

    utils.limpar_tela()
    print(f'''>>> AVALIAÇÃO DOS ALUNOS <<<
-----------------------------------
=> TOTAL:
          
Alunos Aprovados: {alunos_aprovados}
Alunos Reprovados: {alunos_reprovados}

Alunos:  {total_alunos}
-----------------------------------''')

main()