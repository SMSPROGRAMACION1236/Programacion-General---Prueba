
"""Ejercicio 2: Saludo personalizado

Modifica el ejercicio anterior para que el endpoint acepte un nombre como parte de la dirección web.
Por ejemplo, si alguien visita /saludar/Ana, la aplicación debería responder con un saludo personalizado: {"mensaje": "¡Hola Ana!"}."""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return "Esto es la raiz"
@app.get("/saludar")
async def root():
  return "Hola General"

@app.get("/saludar/ana")
async def root():
  return "Hola Ana"