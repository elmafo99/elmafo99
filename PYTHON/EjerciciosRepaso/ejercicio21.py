# Crea una lista nueva con todas las combinaciones de las siguientes dos listas:

# ejer_21_1 = ["Hola", "amigo"]

# ejer_21_2 = ["Que", "tal"]

# Obten el siguiente output:

# ['Hola Que', 'Hola tal', 'amigo Que', 'amigo tal']

resultado = []

ejer_21_1 = ["Hola", "amigo"]
ejer_21_2 = ["Que", "tal"]

for elemento1 in ejer_21_1:
    for elemento2 in ejer_21_2:
        resultado.append(elemento1 + " " + elemento2) # .append agrega la combinación a la lista, en este caso a "resultado"

print(resultado)
