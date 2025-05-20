def conversao():
    temp_f = float(input("Informe a tempoeratura(°F): "))
    temp_c = (5*temp_f - 160)/9
    print(f'{temp_f:.1f}°F equivale a {temp_c:.1f}°C')

conversao()