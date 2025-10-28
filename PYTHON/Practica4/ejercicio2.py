# Ejercicio 2. TRY AND EXCEPT

# Crea un programa que divida dos números introducidos por el usuario. 
# Utiliza try y except para manejar posibles errores de división por cero. 
# Si se produce un error, imprime "No se puede dividir por cero". Si no, imprime el resultado.

try:
    numerador = float(input("Introduce un primer número: "))
    denominador = float(input("Introduce un segundo número: "))
    resultado = numerador/denominador
except:
    ZeroDivisionError
    print("No se puede dividir por 0")

else:
    print(f"Resultado: {resultado}")