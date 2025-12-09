# Ejercicio 17

# En este ejercicio vamos a crear otro juego sencillo. 
# Se trata de intentar adivinar una palabra secreta entre dos intentos. 

# Pasos a seguir:

# - Declara la palabra secreta en una variable
# - Declara una variable para el número de intentos, 
# e implementa un bucle while que verifique que aún hay intentos restantes.
# - Dentro del bucle, solicita al usuario que introduzca una palabra y compárala con la palabra secreta.
# - Si el usuario acierta, imprime "Has ganado" y sal del bucle.
# - Si se acaban los intentos sin acertar, imprime "Lo siento, has perdido".

palabraSecreta = "Tomate"
numeroIntentos = 3

while numeroIntentos >=1:
    palabraUsuario = input("Introduce una palabra: ")
    if palabraSecreta == palabraUsuario:
        print("Has ganado")
        break
    else:
        numeroIntentos -=1

if numeroIntentos == 0:
    print("Lo siento, has perdido")