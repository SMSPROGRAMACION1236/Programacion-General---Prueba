"""Ejercicio 3: Una lista de cosas favoritas

Crea un endpoint que devuelva una lista pequeña de tus cosas favoritas (por ejemplo, colores, animales, comidas).
La respuesta debería ser en formato JSON, como: {"favoritos": ["azul", "perro", "pizza"]}."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
  return "Informacion de Gustos del Liam"


@app.get("/deportes")
async def root():
  deportes = {"deportes":["Futbol", "Padel", "Golf"]}
  return deportes



@app.get("/libros")
async def root():
  libros = {"libros":["Inteligencia Emocional", "Habitos Atomicos", "El Poder del Porque"]}
  return libros
