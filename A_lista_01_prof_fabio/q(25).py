def convert():
    valor_m = int(input("\nInforme um valor em metros(m): "))
    valor_km = valor_m // 1000
    new_valor_m = valor_m % 1000
    print(f'{valor_m}m equivale a {valor_km:.0f}km e {new_valor_m:.0f}m')

convert()