"""Ejercicio 9: Devuelve un mensaje aleatorio

Crea una lista de mensajes cortos y divertidos.
Crea un endpoint que elija uno de estos mensajes al azar y lo devuelva cada vez que se visite. Por ejemplo, la respuesta podría ser {"mensaje": "¡Hoy va a ser un gran día!"} o {"mensaje": "¡Sigue aprendiendo!"}."""


from fastapi import FastAPI
import random as rdm

app = FastAPI()


@app.get("/")
async def main():
  return "Hola Mundo"

@app.get("/mensaje")
async def tipos_mensajes():
  mensajes = ["Hola, que tal", "Buen Dia", "Buenas Tardes"]
  return mensajes

@app.get("/mensaje/{message}")
async def mostrar_mensaje(message:str):
  mensajes = ["Hola, que tal", "Buen Dia", "Buenas Tardes"]
  if message in mensajes:
    return {"mensaje":message}