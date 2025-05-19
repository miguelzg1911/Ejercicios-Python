# Pide una letra y muestra si no es igual a "a", "e", "i", "o" ni "u".

letra = input("Ingresa una letra: ")

letras = ["a","e","i","o","u"]

if letra in letras:
    print("La letra es igual a esta vocal:",letra)
else:
    print("La letra no es igual")
