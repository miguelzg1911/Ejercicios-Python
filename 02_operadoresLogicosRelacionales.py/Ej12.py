# Pide una edad y muestra si es mayor de 17 y menor de 66.

edad = int(input("Ingresa una edad: "))

if edad < 17:
    print("Tu edad es menor de 17")
elif edad > 17 and edad < 66:
    print("Tu edad es mayor que 17 pero menor que 66")
elif edad > 66:
    print("Tu edad es mayor a 66") 

