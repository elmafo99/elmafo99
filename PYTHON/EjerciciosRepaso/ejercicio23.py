# Dada la siguiente lista, elimina todos los valores iguales a 3

# ejer_23 = [3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3]

# TIP: No intentes eliminar elementos sobre la lista que estás iterando. Haz una copia con ejer_5.copy().

ejer_23 = [3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3]

copia = ejer_23.copy()

for elemento in copia:
    if elemento == 3:
        ejer_23.remove(elemento)

print(ejer_23)