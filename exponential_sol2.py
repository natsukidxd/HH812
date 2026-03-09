# A program that accept two integer not greater than ten. first input represent the base of an expontential equation & the second input represents the power. Compute the exponential equation & display the result

# x^n = result
# x = 5, n = 5
# result = x(5) * x(4) * x(3) * x(2) * x(1)
# result = x(n) * x(n - 1)
# result = x * power(x)

from os import system

def main()->None:
    system('cls')
    x:int = int(input('Enter the base: '))
    n:int = int(input('Enter the exponent: '))
    print(f"The result of {x} raised to the power of {n} is {power(x, n)}")

def power(x, n):
    return 1 if n == 0 else x * power(x, n - 1)

if __name__ == "__main__":
    main()