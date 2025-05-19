# Pide dos números y muestra si el primero es mayor y distinto del segundo.

num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa otro numero: "))

if num1 > num2:
    print(f"Este numero '{num1}' es mayor que el numero dos")
elif num1 != num2:
    print(f"Este numero '{num1}' es diferente del numero dos")
else:
    print("Los dos son iguales")


