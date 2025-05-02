#Pide al usuario el día, mes y año por separado e imprime la fecha en formato: "DD/MM/AAAA" y también "AAAA-MM-DD"

Dia = int(input("Ingresa un dia (numeros): "))
Mes = int(input("Ingresa un mes (numeros): "))
Año = int(input("Ingresa un año (numeros): "))

print(f"{Dia}/{Mes}/{Año}")
print(f"{Año}/{Mes}/{Dia}")

