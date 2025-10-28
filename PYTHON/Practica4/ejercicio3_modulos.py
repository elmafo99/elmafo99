# Haz una petición GET a la API pública: https://api.agify.io?name=sofia

# Esta API devuelve una predicción de edad promedio según el nombre.

# Tu programa debe:

# Hacer la petición con requests.get().
# Convertir la respuesta a formato JSON.
# Mostrar por consola:
# El nombre.
# La edad estimada.
# El número de registros usados para calcularla.
# Si ocurre algún error de conexión, mostrar un mensaje:
# "No se pudo conectar con la API"

import requests #antes de intentar imprimir por consola el resultado, hay que hacer pip3 install requestssource venv/bin/activate

url= "https://api.agify.io?name=sofia"

try:
    response = requests.get(url, timeout=10) # Hacer la petición con requests.get().
    response.raise_for_status #lanza error si el status code no es 2xx

    data = response.json() # Convertir la respuesta a formato JSON.

    nombre = data.get("name")
    edad = data.get("age")
    numRegistros = data.get("count")

    print("Nombre: ", nombre)
    print("Edad: ", edad)
    print("Número de registros: ", numRegistros)

except requests.exceptions.RequestException:
    print("No se pudo conectar con la API")

except ValueError:
    print("La respuesta no es un JSON válido") # Por si la respuesta no es JSON válido




