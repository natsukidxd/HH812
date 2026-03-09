'''
	Menu Driven Program
	-------------------
	A program that would display a menu shown below
	
	    MAIN MENU
	------------------
	1. ADDITION
	2. MULTIPLICATION
	3. DIVISION
	4. SUBTRACTION
	0. QUIT/END
	------------------
	ENTER OPTION(0..4):
	provide each option a function that would accept two(2)
	inputs and perform their corresponding operation
'''
from os import system


def input()->None:pass

def addition()->None: 
    system("cls")
    a:int = int(input("Enter first value:"))
    b:int = int(input("Enter second value:"))
    print(f"The sum of {a} and {b} is {(a+b)}")
    
    
def multiplication()->None:
    a:int = int(input("Enter first value:"))
    b:int = int(input("Enter second value:"))
    print(f"The product of {a} and {b} is {(a*b)}")
    
def division()->None: 
    a:int = int(input("Enter first value:"))
    b:int = int(input("Enter second value:"))
    print(f"The quotient of {a} and {b} is {(a/b)}")
    
def subtraction()->None: 
    a:int = int(input("Enter first value:"))
    b:int = int(input("Enter second value:"))
    print(f"The difference of {a} and {b} is {(a-b)}")
    
def displaymenu()->None:
    system("cls")
    print("MAIN MENU".center(18))
    print("-"*18)
    print("1. ADDITION")
    print("2. MULTIPLICATION")
    print("3. DIVISION")
    print("4. SUBTRACTION")
    print("0. QUIT/END")
    print("-"*18)
    
def main()->None: 
    option:int = 99999
    while option !=0:
        displaymenu()        
        option = int(input("Enter Option(0..4):"))
        if option == 1: addition()
        elif option == 2: multiplication()
        elif option == 3: division()
        elif option == 4: subtraction()
        elif option == 0: print("program ended")
        input("Press any to continue...")
    
if __name__=="__main__":
    main()







