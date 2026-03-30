import pwinput
from os import system

username:str = ''
password:str = ''
isAuthenticated = False

def main()->None:
    
    userLogin()
    if isAuthenticated:
        option:int = 99999
        while option != 0:
            displaymenu()
            print(end =' ' * 50)
            option:int = int(input("Enter Option(0..6): "))
            if option == 1: addition()
            elif option == 2: multiplication()
            elif option == 3: division()
            elif option == 4: subtraction()
            elif option == 5: expontential()
            elif option == 6: factorial()
            elif option == 0: print("program ended".center(120, " "))
            input("Press any to continue...".center(120, " "))

    else:
        print("Invalid credentials".center(120, " "))
        [print() for i in range(14)]


def userLogin()->None:
    system('cls')
    global username, password, isAuthenticated
    [print() for i in range(14)]
    print(end =' ' * 50)
    usernameMessage:str = "USERNAME: "
    username = input(usernameMessage)
    print(end =' ' * 50)
    passwordMessage:str = "PASSWORD: "
    password = pwinput.pwinput(passwordMessage)
    [print() for i in range(14)]

    if username == 'admin' and password == 'hello123':
        isAuthenticated = True

def displaymenu()->None:
    system('cls')
    menuitems:list=[
        "1. ADDITION      ",
        "2. MULTIPLICATION",
        "3. DIVISION      ",
        "4. SUBTRACTION   ",
        "5. EXPONENTIAL   ",
        "6. FACTORIAL     ",
        "0. QUIT/END      ",
    ]
    
    [print() for i in range(0,15-len(menuitems))]
    print("MENU".center(120, "-"))
    print()
    [print(menuitems[i].center(120,' ')) for i in range(0,len(menuitems))]

def addition()->None: 
    system("cls")
    [print() for i in range(12)]
    print(end =' ' * 49)
    a:int = int(input("Enter first value: "))
    print(end =' ' * 49)
    b:int = int(input("Enter second value: "))
    print(f"The sum of {a} and {b} is {(a+b)}".center(120, " "))
    [print() for i in range(12)]
    
def multiplication()->None:
    system("cls")
    [print() for i in range(12)]
    print(end =' ' * 49)
    a:int = int(input("Enter first value: "))
    print(end =' ' * 49)
    b:int = int(input("Enter second value: "))
    print(f"The product of {a} and {b} is {(a*b)}".center(120, " "))
    [print() for i in range(12)]
    
def division()->None: 
    system("cls")
    [print() for i in range(12)]
    print(end =' ' * 49)
    a:int = int(input("Enter first value: "))
    print(end =' ' * 49)
    b:int = int(input("Enter second value: "))
    print(f"The quotient of {a} and {b} is {(a/b)}".center(120, " "))
    [print() for i in range(12)]
    
def subtraction()->None: 
    system("cls")
    [print() for i in range(12)]
    print(end =' ' * 49)
    a:int = int(input("Enter first value: "))
    print(end =' ' * 49)
    b:int = int(input("Enter second value: "))
    print(f"The difference of {a} and {b} is {(a-b)}".center(120, " "))
    [print() for i in range(12)]

def expontential()->None:
    system("cls")
    [print() for i in range(12)]
    print(end =' ' * 46)
    a:int = int(input("Enter first value as base: "))
    print(end =' ' * 44)
    b:int = int(input("Enter second value as exponent: "))
    print(f"{a} to the power of {b} is {power(a, b)}".center(120, " "))
    [print() for i in range(12)]

def power(x, n):
    return 1 if n == 0 else x * power(x, n - 1)

def factorial()->None:
    system("cls")
    [print() for i in range(12)]
    print(end =' ' * 47)
    a:int = int(input("Enter a positive integer: "))
    print(f"The factorial of {a} is {factorialCalculation(a)}".center(120, " "))
    [print() for i in range(12)]

def factorialCalculation(x):
    return 1 if x == 0 else x * factorialCalculation(x - 1)

if __name__ == "__main__":
    main()