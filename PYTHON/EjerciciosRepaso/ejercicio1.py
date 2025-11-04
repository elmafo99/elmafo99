# Ejercicio 1

# Crea una función que determine qué debe hacer el usuario, según la hora del día. 
# El usuario debe ingresar por consola qué hora es (slo la hora, no los minutos), 
# y el programa le debe decir qué está agendado a esa hora. La casuística es la siguiente:

# Si es entre las 0 y las 8, print "Durmiendo"
# Si es entre las 9 y las 18, print "Trabajando"
# Si es entre las 19 y las 21, print "Clase"
# Si es entre las 22 y las 24, print "Descanso"
# En cualquier otro caso, print "Transporte o error"
# Implementa mediante sentencias if/elif/else.

def estado():

    hora= int(input("Ingresa la hora: "))

    if 0 <= hora <= 8:
        print("Durmiendo")
    elif 9 <= hora <= 18:
        print("Trabajando")
    elif 19 <= hora <= 21:
        print("Clase")
    elif 22 <= hora <= 24:
        print("Descanso")
    else:
        print ("Transporte o error")

estado()