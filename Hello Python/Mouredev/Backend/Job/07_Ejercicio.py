"""Ejercicio 9: Verifica la longitud de una cadena

Crea un endpoint que acepte una cadena de texto como parte de la dirección web.
La aplicación debe devolver la longitud de esa cadena. Por ejemplo, si alguien visita /longitud/Hola, la respuesta debería ser {"longitud": 4}."""


from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def main():
  return "Has iniciado a mi pagina"
@app.get("/longitud")
async def longitud():
  return "Has entrado a la pagina de longitud"

@app.get("/longitud/{word}")
async def contar_caracteres(word:str):
  return {"longitud": len(word)}