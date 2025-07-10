def main():
    x = int(input())
    y = int(input())
    soma = 0

    if x > y:
        new_x = x
        x = y
        y = new_x

    for i in range (x + 1, y, 1):
        if i % 2 != 0:
            soma += i
            
    print(soma)


main()