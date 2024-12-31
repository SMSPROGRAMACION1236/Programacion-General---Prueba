""" Es un formato para intercambiar datos entre sistemas, para que se puedan comunicar diferentes sistemas, lo que hace es intercambiar informacion, es bastante es legible, facil de usar, y el tamaño de dato es bastante pequeño por lo que es muy eficiente, y es un estandar, por lo que varios lenguajes de programacion lo usan"""
#! Antes tenemos que mirar que es un JSON
### 
""" Es parecido a un diccionario de clave valor
Entre llaves y dos puntos"""

{
    "clientes": [
        {
      "id": 1,
      "nombre": "Juan",
      "edad": 25
      },
      {
        "id": 2,
        "nombre": "Pedro",
        "edad": 30
      }
    ]
}

#* Ejemplo Practico
import requests
### Url que nos permite hacer una solicitud de una foto de un gato
url = "https://api.thecatapi.com/v1/images/search" ### Este como tal seria la URL

## Realizar la operacion GET para obtenerlo
response = requests.get(url)
### Si la respuesta es exitosa
if response.status_code == 200:
  # Convertimos de JSON a un diccionario de python
  data = response.json()
  print(data)
  # Extraemos la URL de la imagen del gato
  image_url = data[0]['url'] ### Apartir del JSON obtenido, podremos acceder a alguna informacion, por ejemplo en este caso la URL
  # Imprime la url de la imagen
  print(image_url)
else:
  print(f"Error: {response.status_code}")


