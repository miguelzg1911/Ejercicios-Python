#Pide un número de tres cifras (ej. 123) y muestra sus cifras en orden inverso (321).Usa operaciones matemáticas para extraer centenas, decenas y unidades.
num = int(input("Ingresa un numero de tres cifras: "))
unidades = num % 10
decenas = (num // 10) % 10
centenas = num // 100
print("C:",unidades, "D:",decenas, "U:",centenas)