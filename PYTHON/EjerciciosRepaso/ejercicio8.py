# Ejercicio 8

# Implementa un programa que imprima por pantalla el siguiente patrón

# 5 4 3 2 1

# 4 3 2 1

# 3 2 1

# 2 1

# 1

# NOTA: NO hay lineas en blanco entre una línea y otra.

for primerNumero in range(5, 0, -1):
    for numeroLista in range(primerNumero, 0, -1):
        print(numeroLista, end=" ")
    print()
        
