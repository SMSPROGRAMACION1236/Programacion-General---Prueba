"""Ejercicio 7: Un contador simple

Crea un endpoint que mantenga un contador.
Cada vez que se visite el endpoint, debería mostrar el valor actual del contador y luego incrementarlo en uno. La primera vez que se visite, debería mostrar {"contador": 1}, la segunda vez {"contador": 2}, y así sucesivamente"""



from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Bienvenido al Contador"}

# Global variable to persist the counter value across requests
contador = 0

@app.get("/contador")
async def contador_endpoint():
  global contador
  contador += 1
  return contador
  