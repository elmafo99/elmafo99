#Utilizar cursor para utilizar PostgreSQL

#EJEMPLO 
#Creamos una función, en este caso, llamada "nuevoIntento" que tiene 5 parámetros (las columnas de nuestra tabla: palabra, letras_acertadas, letras_falladas, intentos)
# Hacemos un try and except, para que en caso de que al insertar un intento haya un error, sepamos donde está el error
# cursor:
# 1. conectamos el cursor, es decir, el elemento que nos va a permitir dar órdenes desde Python a PostgreSQL
# 2. el cursor comienza a funcionar, en este caso, añadiendo los elementos que le estamos pidiendo a nuestra tabla
# los VALUES son los datos que hemos extraído a partir del script de python
# 3. cerramos el cursor IMPORTANTE
# 4. hacemos commit, es decir, confirmamos los cambios en la base de datos. el commit hace que el insert sea permanente

def nuevoIntento(conexion, palabra, letras_acertadas, letras_falladas, intentos):
    try:
        cursor = conexion.cursor()
        cursor.execute(""" 
        INSERT INTO resultados_ahorcado (palabra, letras_acertadas, letras_falladas, intentos)
        VALUES (%s, %s, %s, %s); """, (palabra, letras_acertadas, letras_falladas, intentos))
        cursor.close()
        conexion.commit()
    except Exception as e:
        print("Error al insertar intento:" e)