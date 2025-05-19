# Pide un número decimal y muestra si es negativo o mayor que 100.

num = float(input("Ingresa un numero: "))

if num < 0:
    print("El numero es menor que cero")
elif num > 100:
    print("El numero es mayor que 100")
else:
    print("El numero esta entre el 0 y el 100")
