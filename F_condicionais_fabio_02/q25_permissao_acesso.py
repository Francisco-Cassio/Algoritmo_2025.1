from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    senha = obter_numero_inteiro('Digite a senha: ')
    senha_correta = 1234

    linhas()

    if verificar_senha(senha, senha_correta):
        print('Acesso Liberado!')
    else:
        print('Acesso Negado!')

def verificar_senha(senha: int, senha_correta: int):
    return senha == senha_correta


main()