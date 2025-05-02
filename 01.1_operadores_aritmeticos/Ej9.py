#Pide una cantidad de minutos y muestra a cuántos días, horas y minutos equivale.

Minutos = int(input("Ingresa una cantidad de minutos: "))

Dia = Minutos // 1440
Hora = (Minutos % 1440) // 60
minuto = Minutos % 60

print(f"Dia/s: {Dia}, Hora/s: {Hora}, Minuto/s: {minuto}")
