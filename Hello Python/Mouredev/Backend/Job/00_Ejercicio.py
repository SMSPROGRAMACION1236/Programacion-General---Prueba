
"""Ejercicio 1: Un saludo simple

Crea una aplicación FastAPI que tenga un único "endpoint" (una dirección web).
Cuando alguien visite ese endpoint, la aplicación debería responder con un saludo simple, por ejemplo: {"mensaje": "¡Hola desde FastAPI!"}."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return "Hola desde FastAPI"
