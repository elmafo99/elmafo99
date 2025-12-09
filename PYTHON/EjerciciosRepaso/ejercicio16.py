# Ejercicio 16

# Implementa un programa que imprima por pantalla el siguiente patrón:

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# NOTA: No debe haber espacios al final de cada línea.


for i in range(1, 6):
    linea = ""
    for j in range(1, i+1):
        linea = linea + str(j) + " "
    linea = linea.strip()

    print(linea)

