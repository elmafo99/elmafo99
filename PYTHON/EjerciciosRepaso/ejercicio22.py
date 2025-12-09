# Ejercicio 22

# Dada la siguiente lista, encuentra por el índice el valor 45 y sustitúyelo por el 0

ejer_22 = [20, 47, 19, 29, 45, 67, 78, 90]

indice = ejer_22.index(45) #busca en la lista el primer elemeento que sea 45
ejer_22[indice] = 0 #accede al elemento y lo reemplaza por 0
print(ejer_22) #muestra la lista actualizada