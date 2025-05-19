# Pide una calificación del 0 al 10 y muestra si es válida (entre 0 y 10, sin incluir extremos).

calificacion = float(input("Ingresa una calificacion del 0 al 10: "))

if calificacion <=0 or calificacion >= 10:
    print("Tu calificacion no es valida")
else:
    print("Tu calificacion es valida")

