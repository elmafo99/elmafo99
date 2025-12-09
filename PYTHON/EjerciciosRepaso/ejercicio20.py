# Eleva todos los elementos de la lista al cuadrado

# ejer_2 = [1,2,3,4,5]

# Cómo lo harías con numpy?

ejer_2 = [1,2,3,4,5]

for elemento in ejer_2:
    print(elemento**2)

# -----------------------------------------------------------

# "brew install numpy" en consola para que funcione esa librería

import numpy as np #as np es un alias para no tener que escribir numpy cada vez
ejer_2 = [1,2,3,4,5]

arr = np.array(ejer_2)
cuadrados = arr ** 2

print(cuadrados)

# # Un array (o arreglo) es una estructura de datos que almacena múltiples elementos del mismo tipo en una sola variable, 
# # de forma contigua en memoria.
# En Python, usando NumPy, 
# un array funciona como una lista avanzada que permite hacer operaciones matemáticas de manera eficiente 
# sobre todos sus elementos al mismo tiempo.
