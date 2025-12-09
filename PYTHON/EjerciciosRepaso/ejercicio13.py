# Ejercicio 13

# Escribe un programa que tenga dos variables: 
# un string (pedido al usuario a través de input) 
# y una lista de strings ["Python", "java", "codigo", "ejemplo", "Mundo", "azul"]. 
# El programa debe recorrer la lista e imprimir por pantalla cada elemento de la lista concatenado con el string, pero:

# Si la palabra dada por el usuario empieza con vocal, deberás convertirla a MAYÚSCULAS.
# Caso contrario, debe empezar con mayúsculas y luego minúsculas Luego comprueba
# Si la palabra tiene más de 4 letras, deberás eliminar las letras "r", "s", "l" o "m" que tenga.
# Si tiene 4 letras o menos, agrega una carita felis ":)" luego de ésta.

def Programa():
    palabraUsuario = input("Escribe una palabra: ")
    palabraLista = ["Python", "java", "codigo", "ejemplo", "Mundo", "azul"]

    vocales = "aeiouáéíóú"

    if palabraUsuario[0].lower() in vocales:
        palabraUsuario_cambiada = palabraUsuario.upper()
    else:
        palabraUsuario_cambiada = palabraUsuario[0].upper() + palabraUsuario[1:].lower()


    for elementoLista in palabraLista:

        elementoProcesado = elementoLista
    
        if len(elementoProcesado) > 4:
            elementoProcesado = elementoProcesado.replace("r", "")
            elementoProcesado = elementoProcesado.replace("s", "")
            elementoProcesado = elementoProcesado.replace("l", "")
            elementoProcesado = elementoProcesado.replace("m", "")
        else:
            elementoProcesado = elementoProcesado + ":)"
    
        resultadofinal = elementoProcesado + palabraUsuario_cambiada
        print(resultadofinal)

Programa()