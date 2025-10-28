# Te lo encontrarás mucho en el futuro: 
# la librería random, muy utilizada para generar números o resultados aleatorios, 
# o "pseudoaleatorios", ya que en verdad funcionan internamente en base a algoritmos 
# (es decir, no salen de la nada, sino que Python usa unos cálculos internos para crearlos). 
# Si te interesa, puedes investigar un poquito sobre las distintas funciones de la librería: 
# random(), randint(), randrange(), etc. (Un recurso sencillo y explicativo con ejemplos y explicaciones es este)

import random

#En los notebooks puedes conocer información sobre las librerías. Hay que poner el nombre de la librería y ??.
#Por ejemplo, en este caso pondríamos random??

#Una librería nos permite utilizar funciones entre otras cosas listas para usar, sin tener que inventar nada. 
# Porque nosotros tenemos instalado Python, pero Python diríamos que es lo "básico". Es como si dijeramos que nosotros sabemos sumar,
# pero de repente adquirimos un libro donde están las fórmulas para integrar, derivar, dividir... y lo metemos en nuestro cerebro,
# de forma que ya sabemos hacer todo lo anterior. 

#Por ejemplo, 
# - numpy: nos permite usar grandes datos numéricos de forma fácil; 
# - pandas: nos permite organizar los datos como si fueran hojas excel;
# - random: genera números aleatorios o elige cosas al azar

# Si no queremos instalar la librería en nuestra versión de Python, cabe la posibilidad de utilizar Google Colaboratory (o Google Colab),
# lo cual permite ejecutar código Python sin tener que instalarnos todas las librerías que por ejemplo hemos mencionado anteriormente. 


# Ejercicio 4

# Intentaremos adivinar una palabra secreta entre una lista de opciones. 
# Tienes tres intentos para acertar la palabra correcta. Sigue estos pasos:

# Utilizaremos la función `choice` de la librería random, 
# que devuelve un elemento random de una secuencia dada (como cualquier función, se le debe pasar como argumento).
# En esta función ya viene implementado cómo seleccionar la palabra secreta. Tú le provees la lista, 
# te propongo como ejemplo cinco palabras: ['montaña', 'jardín', 'viento', 'fuego', 'corazón'].

# Declara una variable que represente el número de vidas (intentos) y establece su valor en 3.
# Mediante un bucle while, comprueba que todavía quedan intentos.
# Dentro del bucle, pide al usuario que introduzca su palabra y comprueba si es la palabra secreta. 
# Si no lo es, actualiza el número de intentos.
# Si el usuario acierta la palabra secreta, sal del bucle e imprime "You win". 
# Si se quedan sin intentos, sal del bucle y muestra "You lose".
# TIP: te puede ser útil usar la sentencia else del bucle while para manejar el caso en que pierdas.

# Las primeras líneas del código deberían ser algo así:

lista = ["montaña", "jardín", "viento", "fuego", "corazón"]
palabra_aleatoria = random.choice(lista)

vidas = 3

while vidas > 0:
    intento = input("Adivina la palabra secreta: ")

    if intento == palabra_aleatoria:
        print(f"Correcto! La palabra es {palabra_aleatoria}")
        break
    else: 
        vidas = vidas-1
        print(f"Incorrecto! La palabra {intento} es incorrecta. Has perdido 1 vida. Te quedan {vidas} intentos")
else:
    print(f"You lose. La palabra secreta era {palabra_aleatoria}")
    exit








