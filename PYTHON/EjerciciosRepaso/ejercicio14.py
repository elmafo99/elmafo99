# Ejercicio 14

# Dada la siguiente lista:

# list2 = [25, 35, 45, 55, 65, 75, 85, 95, 105, 115]

# Implementa un programa que los recorra e imprima por pantalla solo los divisibles por 15. 
# Si nos encontramos con uno mayor que 100, detén el bucle.

list2 = [25, 35, 45, 55, 65, 75, 85, 95, 105, 115]

for elemento in list2:
    if elemento > 100:
        break
    if elemento % 15 == 0:
        print(elemento)
    

