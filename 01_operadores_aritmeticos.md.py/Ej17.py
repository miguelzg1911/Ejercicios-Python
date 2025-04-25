#Pide dos números y muestra si al menos uno es mayor que 10 (usar or).

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
if num1 > 10 or num2 > 10:
    print("Al menos uno de los dos numeros es mayor de 10")
else:
    print("Ninguno es mayor de 10")

