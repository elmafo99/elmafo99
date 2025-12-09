# Ejercicio 18

# Crea un programa que divida dos números introducidos por el usuario. 
# Utiliza try y except para manejar posibles errores de división por cero. 
# Si se produce un error, imprime "No se puede dividir por cero". Si no, imprime el resultado.

def NumerosUsuario():
    numero1 = int(input("Introduce un número: "))
    numero2 = int(input("Introduce un número: "))

    try:
        resultado = numero1/numero2
        print(resultado)
    except: 
        ZeroDivisionError
        print("No se puede dividir por 0")

NumerosUsuario()