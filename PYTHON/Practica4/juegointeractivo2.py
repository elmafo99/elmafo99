# Ejercicio 5

# Utilizaremos ahora la función randint de la librería random, que devuelve un número integer, 
# seleccionado del rango especificado como argumento (start y stop). Puedes verlo aquí

# En este ejercicio vamos a crear un contador interactivo. 
# El objetivo es lograr alcanzar un número a través de sumas consecutivas, con un límite de intentos.

# Entonces: el número objetivo lo elige la función, 
# generándolo de manera aleatoria entre los valores indicados usando la librería random. Sigue los pasos:

# Declara la variable del número objetivo, puede ser así: objetivo = random.randint(15, 25)

# Declara una variable para llevar el total (total) e inicialízala en 0.

# También declara una variable para el número de intentos (intentos) y establece su valor en 5.

# Mediante un bucle while, comprueba que todavía quedan intentos y que el total es menor que el número objetivo.

# Dentro del bucle, pide al usuario que introduzca un número entre 1 y 5. Suma ese número al total y actualiza los intentos.

# Si el total alcanza o supera el número objetivo, imprime "Has alcanzado el objetivo!". 
# Si los intentos se acaban sin alcanzar el objetivo, imprime "Te has quedado sin intentos. Prueba de nuevo".

# TIP 1: Usa la sentencia else del bucle while para gestionar el mensaje cuando no se logra alcanzar el objetivo tras agotar los intentos.

# Tip 2, y un poquito más de teoría:

# Cuando pedimos al usuario que escriba un número, Python recibe ese dato inicialmente como texto (string). 
# Si queremos usarlo como número -para hacer operaciones matemáticas como aquí, debemos convertirlo a int().
# Pero si el usuario escribe algo que no es un número válido, como una letra, 
# podemos programar que se lance error llamado ValueError.
# Así, para evitar que el programa se cierre por ese error, usamos un pequeño bloque llamado try-except: 
# dentro de try ponemos la instrucción que puede fallar (como convertir el texto a número), 
# y en except ValueError le decimos qué hacer si aparece ese error 
# (por ejemplo, mostrar un mensaje para que intente de nuevo). 
# Con esto, el programa sigue funcionando sin problema.

import random 

try:
    texto = input("Escribe algo que debería ser un número: ")
    numero = int(texto)
    print(f"El número que escribiste es {numero}")
except ValueError:
    print("Escribe solo números")


objetivo = random.randint(15, 25)

total = 0
intentos = 5

while intentos > 0 and total < objetivo:
    try:
        numero = int(input("Introduce un número del 1 al 5: "))
    except ValueError:
        print("Por favor, introduce un número válido")
        continue

    if 1<= numero <=5:
        total += numero
        intentos -= 1
        print(f"Total actual: {total}. Te quedan {intentos} intentos")
    else:
        print("Número fuera de rango. Intenta otra vez")

if total >= objetivo:
    print("Has alcanzado el objetivo!")
else: 
    print("Te has quedado sin intentos. Prueba de nuevo")
exit
