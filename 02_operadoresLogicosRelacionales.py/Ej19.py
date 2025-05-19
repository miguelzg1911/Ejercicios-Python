# Pide dos números y muestra si el primero no es múltiplo del segundo.

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

if num1 % num2 == 0:
    print(f"El numero {num1} uno es multiplo del numero {num2}")
else:
    print("No es multiplo")


