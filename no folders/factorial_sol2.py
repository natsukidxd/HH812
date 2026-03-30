from os import system

def main()->None:
    system('cls')
    x:int = int(input("Enter a positive integer less than 20: "))
    if x > 0 and x < 21:
        print(f"The factorial of {x} is {factorial(x)}")
    else:
        print("Invalid input")

def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

if __name__ == "__main__":
    main()