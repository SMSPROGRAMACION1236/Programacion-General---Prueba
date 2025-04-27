"""Ejercicio 4: Suma sencilla

Crea un endpoint que acepte dos números como parte de la dirección web.
La aplicación debería tomar esos dos números, sumarlos y devolver el resultado. Por ejemplo, si alguien visita /sumar/5/3, la respuesta debería ser: {"resultado": 8}."""


from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
  return "Esta es la raiza"


@app.get("/suma/")
async def root(num1= 0, num2= 0):
  num1 = int(input("Ingresa el primer numero: "))
  num2= int(input("Ingresa el segundo numero: "))
  return f"El resultado de la suma es: {num1 + num2}"

