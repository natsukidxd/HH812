'''
	display 'i love you' at the center
	of the screen
'''
from os import system

def displaymenu()->None:
    system('cls')
    menuitems:list=[
        "1. ADDITION      ",
        "2. MULTIPLICATION",
        "3. DIVISION      ",
        "4. SUBTRACTION   ",
        "5. EXPONENTIAL   ",
        "6. FACTORIAL     ",
    ]
    
    [print() for i in range(0,15-len(menuitems))]
    [print(menuitems[i].center(120,' ')) for i in range(0,len(menuitems))]
    
def main()->None:
    displaymenu()
    option:int = int(input("Enter Option(0..6):".center(120,' ')))
    # message:str = 'i love you'
    # [print() for i in range(0,14)]
    # print(message.upper().center(120,' '))
    # [print() for i in range(0,14)]
if __name__=="__main__":
    main()