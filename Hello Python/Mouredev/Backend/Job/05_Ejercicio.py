"""Ejercicio 6: Elige un color

Crea un endpoint que devuelva un color de una lista pequeña de colores predefinidos (por ejemplo, rojo, verde, azul).
Cada vez que se visite el endpoint, debería devolver un color diferente de la lista."""


from fastapi import FastAPI
import random as rdm


app = FastAPI()

@app.get("/")
async def root():
  return "Bienvenido a los colores aleatorios"
  
@app.get("/colors")
async def root():
  colors = ["Red","Blue","Green", "Pink"]
  
  choise = rdm.choice(colors)
  return choise