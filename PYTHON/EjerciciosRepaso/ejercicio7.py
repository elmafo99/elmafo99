# Ejercicio 7

# Escribe un programa en Python que imprima por pantalla todos los números divisibles por 5 y divisibles por 7, 
# dentro del rango de valores (150, 350)

funcionRango = range(150, 351)

# This case is for numbers divisible by 5 on one hand, and by 7 on the other:

for numero in funcionRango:
    if numero %5 == 0:
        print(f"El {numero} es un número divisible por 5")
    if numero %7 == 0:
        print(f"El {numero} es un número divisible por 7")

# This case is for numbers divisible by 5 and by 7 altogether:

for numero in funcionRango:
    if numero %5 == 0 and numero %7 ==0:
        print(f"El {numero} es un número divisible por 5 y por 7")
