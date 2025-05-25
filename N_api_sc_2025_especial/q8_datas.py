# 8. (q8_datas.py) Receba duas datas (dia, mês e ano), e em seguida
# mostre “a distância” entre as duas data no formato “A anos, M
# meses e D Dias”, caso A, M ou D sejam 0, ajustar a frase para
# mostrar apenas a distância correta como, por exemplo, “1 ano e
# 15 dias” ou “30 meses”.
# Restrições: Dias → 1 a 30, Meses → de 1 a 12, e Anos de 1 a 3000

# Ínicio às 10h02 em 25/05

from q1_number_utils import obter_numero_inteiro_min


def main():
    dia_a = obter_numero_inteiro_min('Dia A: ', 0)
    mes_a = obter_numero_inteiro_min('Mês A: ', 0)
    ano_a = obter_numero_inteiro_min('Ano A: ', 0)
    
    dia_b = obter_numero_inteiro_min('Dia B: ', 0)
    mes_b = obter_numero_inteiro_min('Mês B: ', 0)
    ano_b = obter_numero_inteiro_min('Ano B: ', 0)

    A = 0
    B = 0
    C = 0

    if 1 <= ano_a <= 3000 and 1 <= ano_b <= 3000:
        A = ano_a - ano_b if ano_a > ano_b else ano_b - ano_a
    
    if 1 <= mes_a <= 12 and 1 <= mes_b <= 12:
        M = mes_a - mes_b if mes_a > mes_b else mes_b - mes_a
    
    if 1 <= dia_a <= 30 and 1 <= dia_b <= 30:
        D = dia_a - dia_b if dia_a > dia_b else dia_b - dia_a

    
        if D != 0:
            if M != 0:
                if A != 0:
                    print(f'{A} anos, {M} meses e {D} dias')
                else:
                    print(f'{M} meses e {D} dias')
            else:
                if M == 0 and A == 0:
                    print(f'{D} dias')
                else:
                    print(f'{A} anos e {D} dias')
        else:
            if D == 0 and M == 0:
                print(f'{A} anos')
            elif D == 0 and A == 0:
                print(f'{M} meses')
            else:
                print(f'{A} anos e {M} meses')


main()

# Finalizado às 10h32 em 25/05