# Pide una temperatura y muestra si no es inferior a 0 ni superior a 35.

temperatura = float(input("Ingresa una temperatura: "))

if temperatura < 0:
    print("La temperatura esta bajo cero")
elif temperatura > 35:
    print("La temperatura sobrepasa los 35 grados")

