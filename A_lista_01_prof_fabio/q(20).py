def conversao_temperatura():
    temp_c = float(input("Informe a temperatura em °C: "))
    temp_f = (9 * temp_c + 160) / 5
    print(f'{temp_c:.1f}°C equivale a {temp_f:.1f}°F')

conversao_temperatura()