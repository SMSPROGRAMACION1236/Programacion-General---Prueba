"""Ejercicio 8 :Convierte a mayúsculas

Crea un endpoint que acepte una cadena de texto como parte de la dirección web.
La aplicación debe convertir esa cadena a mayúsculas y devolverla. Por ejemplo, si alguien visita /mayusculas/mundo, la respuesta debería ser {"resultado": "MUNDO"}."""


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
  return "Wasaa"

@app.get("/mayusculas")
async def mayusculizacion():
  return "Has entrado a la seccion de mayusculas"

@app.get("/mayusculas/{word}")
async def mayusculizacion(word: str):
  return {"resultado":word.upper()}

