#Pide dos números y muestra si el primero no es igual al segundo (usar not y ==).

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
comparacion = not(num1==num2)
if comparacion == True:
    print("No son iguales")
elif comparacion == False:
    print("Son iguales")

