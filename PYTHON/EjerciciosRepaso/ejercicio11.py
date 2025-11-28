# Ejercicio 11

# Vamos a crear un clasificador de vehículos. Declara las siguientes variables:

# peso
# tipo

# Implementa la siguiente casuística:

# Si el tipo es "Camión" y el peso es superior a 5000 kg, el vehículo es "Vehículo pesado"
# Si el tipo es "Coche" y el peso es más de 2000, el vehículo es "Vehículo pesadito"
# Si el tipo es "Coche" y el peso está entre 1000 kg y 2000 kg, el vehículo es "Vehículo ligero"
# Si el tipo es "Moto" y el peso es mayor a 500, el vehículo es "Vehículo ligero".
# Si el tipo no es "Moto" y el peso es menor de 500 kg, el vehículo es "Vehículo muy ligero"
# En cualquier otro caso, clasifica el vehículo como "Sin clasificación"


def ClasificadordeVehiculos():
    peso = int(input("Introduce el peso del vehículo: "))
    tipo = input("Introduce el tipo de vehículo: ")

    if tipo == "camion" and peso > 5000:
        print("Vehículo pesado")
    elif tipo == "coche" and peso > 2000:
        print("Vehículo pesadito")
    elif tipo == "coche" and 1000 <= peso <= 2000:
        print("Vehículo ligero")
    elif tipo != "moto" and peso <= 500:
        print("Vehículo muy ligero")
    else: 
        print("Sin clasificación")

ClasificadordeVehiculos()