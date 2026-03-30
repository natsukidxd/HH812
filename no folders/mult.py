from os import system

def main()->None:
	system('cls')
	n:int = int(input("Enter n(+n<=20):"))
 
	if n>0 and n<21:
		for i in range(1, n+1):
			for j in range(1, n+1):
				print(f"{i * j: 5}", end = "")
    
			print()
	
	else:
		print("invalid input")


if __name__ == "__main__":
	main()