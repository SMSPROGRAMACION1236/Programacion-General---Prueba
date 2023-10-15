from fastapi import FastAPI  # Importamos fastapi

from routers import products # asi tenemos acceso al fichero de productos

from routers import users
from fastapi.staticfiles import StaticFiles # Para recursos estaticos

app = FastAPI()  # Instanciar fastApi

#Routers
app.include_router(products.router) # Incluimos en el api principal uno de los routers
app.include_router(users.router)  # Lo mismo pero con el otro router

app.mount("/static", StaticFiles(directory="static"), name= "static")

@app.get("/") # Es la raiz

async def root():  # Llama al servidor debe ser asincrota es decir tiene que tener sincronizacion con el servidor
   return "!Hola Mund2o3"


# uvicorn main:app --reload # uvicorn el servidor en donde main es el fichero cual queremos arrancar y app la instancia que queremos arrancar y el --reloand va a cargar el servidor automaticamente



@app.get("/url") # Seria por ejemplo el ip mas santi en el navegador
async def url(): # Lo de azul es una funcion que sirve como variable
   return { "url":"https://mouredev.com/python"} # El estandar es con json
   
   


# Error 404 no found osea que encuentra ese ip
# Error 500 es cuando ha petado o ha caido xd 

# Haciendo /docs nos puede crear documentacion por medio de swagger.iu
# otro es de /redoc te permite descargar all las especificaciones de la api en forma de json


# Detener el server CTRL + C
# POST: para crear datos.
# GET: para leer datos.
# PUT: para actualizar datos.
# DELETE: para borrar 

