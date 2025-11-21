# Ejercicio 6

# Dada la siguiente lista:

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Implementa un programa que los recorra e imprima por pantalla todos los divisibles por 5. 
# Si nos encontramos con alguno que sea mayor que 150, detener el bucle.

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for element in list1:
    if element > 150:
        break
    if element % 5 == 0:
        print(f"{element} es divisible entre 5")


