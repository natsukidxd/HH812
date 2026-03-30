from os import system

system('cls')
count:int = 0

x:int = int(input('input: '))
while x != 9999:
    y:int = int(input('input: '))
    if x < y:
        count = count + 1
    x = y
print(f"result: {count}")