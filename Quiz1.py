from os import system

system('cls')

n:int = int(input("input: "))
y:int = n
if n > 0 and n < 10:
    for i in range(1, n + 1):
        a:int = 1
        
        for x in range(y, 0, -1):
            print(a, end = " ")
            a = a + 1
        y = y - 1
        print()
else:
    print("invalid input")