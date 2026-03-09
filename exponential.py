# A program that accept two integer not greater than ten. first input represent the base of an expontential equation & the second input represents the power. Compute the exponential equation & display the result

from os import system

def main()->None:
    system('cls')
    x:int = int(input('Enter the base: '))
    result:int = 1

    if x > 0 and x < 11:
        n:int = int(input('Enter the exponent: '))
        if n > 0:
            for i in range(1, n + 1):
                result *= x
            print(f"The result of {x} raised to the power of {n} is {result}")
        else:
            print("Invalid input for exponent")
    else:
        print("Invalid input for base")

if __name__ == "__main__":
    main()