#Pide al usuario un número de segundos y muestra cuántas horas, minutos y segundos son.

TSegundos = int(input("Ingresa un numero de segundos: "))

Horas = TSegundos // 3600
Minutos = (TSegundos % 3600) // 60
Segundos = TSegundos % 60

print(f"Segundos Totales son igual a:\n{Horas}:Hora/s {Minutos}:Minuto/s {Segundos}:Segundo/s")


