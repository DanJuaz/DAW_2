# primero instalar requests desde la consola
# conda install requests ; pip install requests

import requests
import json

# URL de la API de JSONPlaceholder para obtener datos de usuarios
url = "https://jsonplaceholder.typicode.com/users"

# Realiza una solicitud GET a la API
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    print(response.text) # el contenido de la respuesta como una cadena de texto.
    # Utiliza json.loads() para analizar la respuesta JSON
    #data = json.loads(response.text)
    data = response.json()
    print("Datos de usuarios de JSONPlaceholder:")
    print(data)
else:
    print(f"Error en la solicitud. Código de respuesta: {response.status_code}")