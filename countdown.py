from os import system

def main()->None:
    system('cls')
    
    n:int = int(input("Enter value: "))
    
    if n > 0 and n < 21:
        
        for i in range(n, 0, -1):
            print(f"{i:5}", end = "")

    else:
        print("invalid input")

if __name__ == "__main__":
    main()