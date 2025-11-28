# Ejercicio 10

# Crea una función para ver qué toca hacer hoy. 
# Pide al usuario que introduzca un número del 1 al 7 por consola, que representará un día de la semana (Lunes a Domingo). 
# Implementa la siguiente casuística con una función:

# Si el número es 6 o 7, imprime "Hoy es fin de semana, vete de fiesta!"
# Si está entre 1 y 4, imprime "Hoy toca currar todo el día"
# Si el número es 5, imprime "Hoy trabaja por la mañana, y estudia por la tarde"
# En cualquier otro caso, imprime "La semana tiene solo 7 días!"

def Tarea():
    numero = int(input("Introduce un número del 1 al 7: "))
    if numero == 6 or numero == 7:
        print("Hoy es fin de semana, vete de fiesta!")
    elif 1 <= numero <= 4:
        print("Hoy toca currar todo el día")
    elif numero == 5:
        print("Hoy trabaja por la mañana, y estudia por la tarde")
    else:
        print("La semana tiene solo 7 días!")

Tarea()