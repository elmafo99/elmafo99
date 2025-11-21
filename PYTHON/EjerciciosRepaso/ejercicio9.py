# Ejercicio 9

# En este ejercicio vamos a crear un pequeño juego. 
# Se trata de intentar adivinar un numero del 1 al 5. Tenemos dos intentos para acertar. 

# Pasos a seguir:

# Ya viene implementado cómo obtener un número aleatorio del 1 al 5
# Tendrás que declarar en una variable el numero de vidas, y mediante un bucle while, comprobar que todavia quedan vidas.
# Dentro del bucle, obtener el valor del usuario y comprobar si es ese el numero a adivinar. Si no, actualizar las vidas.
# Si acertamos, salimos del bucle e imprimimos por pantalla "You win". Y si perdemos también salimos del bucle, 
# pero en este caso imprimimos por pantalla "You lose".
# TIP: te puede resultar útil usar la sentencia else cuando acabe el bucle while. 
# Lo que haya dentro de ese else se ejecutará una vez acabe la ejecución del while. Lo podrás usar para cuando pierdas.

import random 

numeroSecreto = random.randint(1, 5)

vidas = 2

while vidas > 0:
    InsertarNumero = int(input("Inserta un número del 1 al 5: "))
    if InsertarNumero == numeroSecreto:
        print("You win!")
        break
    else:
        vidas = vidas - 1
        if vidas > 0:
            print("Inténtalo de nuevo")
        
else:
    print("You lose")
        

