# Pide tres números y muestra si alguno de ellos es igual a 0.

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
num3 = int(input("Ingresa un numero: "))

if num1 == 0:
    print(f"El primer numero es igual que 0")
elif num2 == 0:
    print(f"El segundo numero es igual que 0")
elif num3 == 0:
    print("El tercer numero es igual que 0")
else: 
    print("Ningun numero es igual que 0")