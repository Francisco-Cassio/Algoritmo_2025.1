def main():
    n = int(input())

    total_coelhos = 0
    total_ratos = 0
    total_sapos = 0

    for _ in range(n):
        exp = input().split()
        quantia = int(exp[0])
        tipo = exp[1].upper()

        if 1 <= quantia <= 15:
            if tipo == 'C':
                total_coelhos += quantia
            elif tipo == 'R':
                total_ratos += quantia
            elif tipo == 'S':
                total_sapos += quantia
            
    total = total_coelhos + total_ratos + total_sapos

    percent_coelhos = (total_coelhos / total) * 100
    percent_ratos = (total_ratos / total) * 100
    percent_sapos = (total_sapos / total) * 100

    print(f'Total: {total} cobaias\nTotal de coelhos: {total_coelhos}\nTotal de ratos: {total_ratos}\nTotal de sapos: {total_sapos}')
    print(f'Percentual de coelhos: {percent_coelhos:.2f} %\nPercentual de ratos: {percent_ratos:.2f} %\nPercentual de sapos: {percent_sapos:.2f} %')
        


main()