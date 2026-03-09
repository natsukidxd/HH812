from os import system

system('cls')

n:int = int(input('Input: '))

if n > 0 and n < 11:
    for i in range(0, n + 1):
        
        for j in range(1, (n - i) + 1):
            print(j, end = " ")

        print()

else:
    print('Invalid')
