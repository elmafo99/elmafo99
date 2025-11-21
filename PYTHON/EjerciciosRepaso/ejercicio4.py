# Ejercicio 4

# Escribe una función que le pida al usuario un número del 1 al 100.

# Tienes una variable lista = [2, 3, 4, 5, 6].

# El programa debe comprobar que el usuario introduce un número válido. Y luego lo siguiente:

# Si el número es entre 1 y 30, debe ser multiplicado por la lista de números. 
# El programa debe recorrer la lista e imprimir por pantalla cada elemento de la lista multiplicado por el número uno bajo el otro, 
# separados con este separador: "|"
# Si el número es mayor a 30 y menor a 60, debe ser elevado por esa lista.
# Si el número es igual o mayor a 60 e igual o menor que 100, debe dividirse por los números de esa lista.
# Si es mayor a 100, debe lanzar mensaje de error. Esto lo puedes hacer con ifs, o practicar el try/except!
# Recuerda documentar las funciones, de a poco ir implementando buenas prácticas!

lista = [2, 3, 4, 5, 6]

def insertarNumero():
    try:
        numero = int(input("Inserta un número del 1 al 100: "))
    except ValueError:
        print("Debes introducir un número válido")
        return

    if numero <1 or numero >100:
        print("Error. Debes insertar un número mayor que 1 y menor que 100")
        return
    
    elif 1 <= numero <= 30:
        print("Multiplicación: ")
        for elemento in lista:
            print(f"{elemento*numero}|")

    elif 30 < numero <=60:
        print("Potencia: ")
        for elemento in lista:
            print(f"{numero**elemento}|")
    
    elif  60 < numero <=100:
        print("División: ")
        for elemento in lista:
            print(f"{numero/elemento}|")
            

insertarNumero()



