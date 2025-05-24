"""Ejercicio 11: Simula un lanzamiento de dado

Crea un endpoint que simule el lanzamiento de un dado de seis caras.
Cada vez que se visite el endpoint, debería devolver un número aleatorio entre 1 y 6. La respuesta podría ser {"resultado": 3} o {"resultado": 6}, etc."""


from fastapi import FastAPI
import random as rdm
app = FastAPI()
@app.get("/")
async def main():
  return "Hola Ejercicio 10"


@app.get("/aleatorio")
async def numero_aleatorio():
  selection = rdm.randint(1,6)
  return selection