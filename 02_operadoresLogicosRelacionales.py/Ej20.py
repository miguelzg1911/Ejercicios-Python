# Pide un número y muestra si es igual a 0, o si es mayor que 10 y menor que 20.

num = int(input("Ingresa un numero: "))

if num == 0:
    print("El numero es igual a cero")
elif num > 10 and num < 20:
    print("El numero esta en un rango entre 10 y 20")
else:
    print("El numero es diferente")

