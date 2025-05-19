# Pide una edad y muestra si está fuera del rango de 0 a 120.

edad = int(input("Ingresa una edad: "))

if edad < 0 or edad > 120:
    print("La edad esta fuera del rango entre 0 y 120 años")
else:
    print("Si esta en el rango")


