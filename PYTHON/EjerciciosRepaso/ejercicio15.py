# Ejercicio 15

# Escribe un programa que imprima por pantalla todos los números que sean múltiplos de 3 y de 4, 
# dentro del rango de valores (50, 150).


for elemento in range(50, 150):
    if elemento % 3 == 0 and elemento % 4 == 0:
        print(elemento)