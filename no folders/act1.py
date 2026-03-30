#Ferrer, Krist Dave B.

from os import system

def main()->None:
    system('cls')
    
    sum:int = 0

    for i in range(5):
        try:
            x:int = int(input(f"{(i + 1)}. Enter an even integer: "))
            
            if x < 10:
                if (x % 2 == 0):
                    sum = sum + x
            
                else:
                    print(f"Error: not an even integer")
                    break
                
            else:
                print(f"Error: Value is greater than or equal to 10")
                break
        except Exception as e:
            print(f"Error: {e}")
            break
         
    print(f"The sum is {sum} and the average is {(sum / 5)}")

if __name__ == "__main__":
    main()