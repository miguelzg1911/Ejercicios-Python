#Pide el radio de un círculo y muestra el área y el perímetro (circunferencia).

pi = 3.1416
radio = float(input("Ingresa el radio del circulo: "))

area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"Area del circulo: {area:.2f}")
print(f"Perimetro del circulo: {perimetro:.2f}")
