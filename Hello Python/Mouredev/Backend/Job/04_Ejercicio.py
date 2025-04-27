"""Ejercicio 5: ¿Es un número par?

Crea un endpoint que acepte un número como parte de la dirección web.
La aplicación debe verificar si el número es par o impar y devolver un mensaje indicándolo. Por ejemplo, si alguien visita /es_par/10, la respuesta podría ser: {"resultado": "El número 10 es par"}. Si visita /es_par/7, la respuesta podría ser: {"resultado": "El número 7 es impar"}."""



from fastapi import FastAPI



app = FastAPI()

@app.get("/")
async def root():
  return "Hola Suma"

@app.get("/suma/{num}")
async def  root(num: int):
  if num %2 ==0:
    return "Par"
  else:
    return "Impar"
  
  
  


