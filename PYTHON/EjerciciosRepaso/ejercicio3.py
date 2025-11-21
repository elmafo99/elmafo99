# Ejercicio 3

# En este ejercicio vamos a realizar un programa muy parecido. 
# Para este caso queremos que se cumplan las siguientes condiciones:

# Si el distrito es "Retiro", comprueba si la superficie es mayor de 100 metros cuadrados. 
# En tal caso, que imprima un precio de 1000, y si no, de 500, mas el mensaje "Distrito con $$$".

# Si NO es Retiro, deberá ser un 25% menos, e imprimit "Distrito pobre".
# TIP: Hay que usar ifs anidados.

# Crea tu código siempre con funciones, para que lo puedas reutilizar luego!

def calculadora():
    distrito = str(input("Inserta un distrito: "))
    superficie = int(input("Inserta una superficie: "))

    if distrito == "Retiro":
        if superficie > 100:
            print("precio: 1000")
        elif superficie < 100:
            print("precio:500")
        
        print("Distrito con $$$")
        
    else:
        precio_base = 1000 if superficie > 100 else 500
        precio_desc = precio_base * 0.75
        print(f"precio: {precio_desc}")
        print("Distrito pobre")

calculadora()


