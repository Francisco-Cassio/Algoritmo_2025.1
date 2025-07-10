def main():
    n = int(input())
    
    dentro = 0
    fora = 0

    if n < 10000:
        for _ in range(0 , n, 1):
                x = int(input())
                if -10**7 <= x <= 10**7:
                    if 10 <= x <= 20:
                        dentro += 1
                    else:
                         fora += 1
    
    print(f'{dentro} in')
    print(f'{fora} out')
                          

main()