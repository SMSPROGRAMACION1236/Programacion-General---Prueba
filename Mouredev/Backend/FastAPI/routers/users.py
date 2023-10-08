from fastapi import APIRouter , HTTPException # Para poder poner excepcions de HTTP
from pydantic import BaseModel # Nos da la capacidad de crear una entidad 

router = APIRouter()

@router.get("/usersjson")
# Entidad user

class User(BaseModel):
  id: int
  name : str
  surname : str
  url :str
  age : int

users_list =  [User(id = 1, name="Santi", surname= "sanabria", url = "https://google.com", age = 13),
              User(id = 2, name="alan", surname= "wasaaa", url ="https://google.com",age = 43),
              User(id = 3, name="Santi", surname= "sanabria", url ="https://google.com", age = 23)]

async def usersjson():
  return [{"name":"Santi", "surname": "sanabria", "url":"https://google.com", "age": 13},
  {"name":"alan", "surname": "wasaaa", "url":"https://google.com","age": 43},
  {"name":"Santi", "surname": "sanabria", "url":"https://google.com", "age": 23}]


@router.get("/users")
async def users():
  return users_list


#Parh
@router.get("/user/{id}")
async def user(id: int):
  users =  filter (lambda user: user.id == id, users_list)
 
 

# No se puede poner id 4 ya no existe
  try:
    return list(users)[0]
  except:
    return {"error": "no hay usuario"} # En los casos de sea 4 y asi explica el error
  
#Query

@router.get("/userquery/")
async def user(id: int, name:str): # Si hay mas parametros en el navegador se debe de especificar eso con el & luego el parametro y el valor
  users =  filter (lambda user: user.id == id, users_list)
  return search_user(id)
#query podemos igualar una clave con un valor en una url en donde debemos de tipar todo y usa el signo ?

# @app.post("/user/")
# async def user(user:User):
#   users_list.append(user)   ## This is the facking problem

#Post
@router.post("/user/",response_model=User,status_code=201)  # el parametro status_code sirve para reasignar un error talves por que es lo mejor # response-model es para poner el error en la documentacion
async def user(user:User):
  if type(search_user(user.id)) == User:
      raise HTTPException(status_code=404, detail="El usuario ya existe")
    # Cuando lanzamos un error debe de ser con el raise
  
  users_list.append(user)  # En el cliente en la parte de json debemos de poner los datos 
  return user

#Put

@router.put("/user/")
async def user(user:User):


  found = False
  for index, saved_user in enumerate(users_list):
    if  saved_user.id == user.id:
      users_list[index]=user
      found = True
  if not found:
    return {"error": "no hay actualizacion"}
  return user

# Solo si documento esto me funciona


@router.delete("/user/{id}")
async def user(id: int):

  found = False

  for index, saved_user in enumerate(users_list):
    if  saved_user.id == id:
      del users_list[index]
      found = True
  if not found:
    return {"error": "no hay actualizacion"}
  

  


def search_user(id:int):
   users =  filter (lambda user: user.id == id, users_list)
   try:
    return list(users)[0]
   except:
    return {"error": "no hay usuario"}#Path cuando los parametros son obligatorios
#Query los que pueden ir y los que no
   

# Normalmente usas:

# POST: para crear datos.
# GET: para leer datos.
# PUT: ##Post##para actualizar datos.
# DELETE: para borrar dato

### Pequeña Documentacion ###
    #100y superiores son para "Información". Rara vez los usas directamente. Las respuestas con estos códigos de estado no pueden tener cuerpo.
    # 200y superiores son para respuestas "exitosas". Estos son los que usarías más.
    # 200es el código de estado predeterminado, lo que significa que todo estaba "OK".
    # Otro ejemplo sería 201"Creado". Se usa comúnmente después de crear un nuevo registro en la base de datos.
    # Un caso especial es 204"Sin contenido". Esta respuesta se utiliza cuando no hay contenido para devolver al cliente, por lo que la respuesta no debe tener cuerpo.
    # 300y superiores son para "Redirección". Las respuestas con estos códigos de estado pueden tener o no cuerpo, excepto 304"No modificado", que no debe tenerlo.
    # 400y anteriores son para respuestas de "Error del cliente". Este es el segundo tipo que probablemente usarías con más frecuencia.
    # Un ejemplo es 404, para una respuesta "No encontrado".
    # Para errores genéricos del cliente, puedes usar 400.
    # 500y superiores son para errores del servidor. Casi nunca los usas directamente. Cuando algo sale mal en alguna parte del código de su aplicación o servidor, automáticamente devolverá uno de estos códigos de estado


