# Crea una tupla con 3 elementos
# Crea otra tupla con un elemento y comprueba su tipo
# Crea una tupla con elementos de diferentes tipos
# Imprime por pantalla el primer y último elemento de la tupla del apartado 3. Usa len para el último
# Añade un elemento a la tupla del apartado 3.
# Eliminar un elemento de la tupla del apartado 5, que se encuentre más o menos en la mitad.
# Convierte la tupla del apartado 5 en una lista

tupla1 = ("casa", "coche", "trabajo")

tupla2 = type(2.5)
print(tupla2)

tupla3 = ("casa", 5,8, 6, "hola")
print(tupla3[0])
print(tupla3[len(tupla3[-1])])

listatemporal = list(tupla3)
listatemporal.append('armario')
listatemporal.remove(6)
print(listatemporal)
