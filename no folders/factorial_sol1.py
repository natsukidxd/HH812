from os import system

def main()->None:
    system('cls')

    x:int = int(input("Enter a positive integer less than 20: "))
    if x > 0 and x < 21:
        factorial:int = 1
        for i in range(1, x + 1):
            factorial *= i
        print(f"The factorial of {x} is {factorial}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()