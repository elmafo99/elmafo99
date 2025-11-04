# Ejercicio 2

# En este ejercicio vamos a implementar un calculador de precios de casas muy sencillo. Tenemos las siguientes variables:

# superficie

# distrito

# Implementa mediante sentencias if/elif/else la siguiente casuística:

# Si el distrito es "Moncloa" o "Centro", y además la superficie es superior a 100 metros cuadrados, 
# el precio de la casa es de 1000

# Si el distrito es "Salamanca", y además la superficie de la casa es al menos de 150 metros, el precio de la casa es de 1500

# Si el distrito no es "Retiro" y la superficie está entre 60 y 80 metros, el precio es de 600
# En cualquier otro caso, el precio será de 0
# Crea la calculadora de precios mediante una función que le pida al usuario el distrito y la superficie mediante input. 
# Utiliza los bucles y el control de flujos que consideres adecuados.

# Sé creativo/a con el bot, the sky is the limit!

def calculadora():
    distrito = str(input("Escribe el distrito: "))
    superficie = int(input("Indica la superficie: "))

    if (distrito == "Moncloa" or distrito == "Centro") and superficie >= 100:
        print("El precio de la casa es de 1000")
    elif distrito == "Salamanca" and superficie >= 150:
        print("El precio de la casa es de 1500")
    else:
        print("El precio es 0")

calculadora()

