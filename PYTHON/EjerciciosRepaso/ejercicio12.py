# Ejercicio 12

# Vamos a crear un sistema que determine si un alumno tiene derecho a una beca. Declara las siguientes variables:

# nota
# ingresos

# Implementa la siguiente lógica:

# Si la nota es igual o mayor a 8, imprime "Posible candidato"
# Si es así, comprueba si los ingresos son menores de 20000, en cuyo caso imprime "Beca aprobada". 
# Si los ingresos son superiores, imprime "No cumple los requisitos económicos"
# Si la nota no es mayor de 8, imprime "No cumple los requisitos académicos"

def ProgramaBeca():
    nota = int(input("Introduce una nota: "))
    ingresos = int(input("Introduce los ingresos: "))

    if nota >= 8:
        print("Posible candidato")
        if ingresos < 20000:
            print ("Beca aprobada")
        else:
            print("No cumple los requisitos económicos")
    if nota < 8:
        print("No cumple los requisitos académicos")

ProgramaBeca()