#Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.

CostoComida = float(input("Ingresa el costo de la comida: "))

porcentaje1 = (10/100) * CostoComida
porcentaje2 = (15/100) * CostoComida
porcentaje3 = (20/100) * CostoComida

print(f"El 10% de propina es: {porcentaje1:.2f}, y propina mas costo: {porcentaje1 + CostoComida:.3f}")
print(f"El 15% de propina es: {porcentaje2:.2f}, y propina mas costo: {porcentaje2 + CostoComida:.3f}")
print(f"El 20% de propina es: {porcentaje3:.2f}, y porpina mas costo: {porcentaje3 + CostoComida:.3f}")
