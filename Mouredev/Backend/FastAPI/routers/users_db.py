from fastapi import APIRouter , HTTPException # Para poder poner excepcions de HTTP
from fastapi import status  # Los errores http

from db.models.user import User # Importamos el user en donde esta la clase...
from db.client import db_client
from bson import ObjectId

from db.schemas.user import user_schema, users_schema
router = APIRouter(prefix="/userdb", ## Quiere decir que no es necesario mas adelante indicar la url
                   tags=["userdb"], # Para agrupar en la documentacion
                    responses={status.HTTP_400_BAD_REQUEST: {"message":"no encontrado"}})  #luego poner el error defaut del api


# @router.get("/usersjson")
# # Entidad user


users_list =  []



@router.get("/", response_model=list[User])
async def users():
  return users_schema(db_client.local.users.find()) # Return all in the database


#Path
@router.get("/{id}")
async def user(id: str):
  return search_user("_id",ObjectId(id))
# #   users =  filter (lambda user: user.id == id, users_list)
# # No se puede poner id 4 ya no existe
#   try:
#     return list(users)[0]
#   except:
#     return {"error": "no hay usuario"} # En los casos de sea 4 y asi explica el error

#Query

@router.get("/")
async def user(id: str, name:str): # Si hay mas parametros en el navegador se debe de especificar eso con el & luego el parametro y el valor
  # users =  filter (lambda user: user.id == id, users_list)
  return search_user("_id",ObjectId(id))
#query podemos igualar una clave con un valor en una url en donde debemos de tipar todo y usa el signo ?

# @app.post("/user/")
# async def user(user:User):
#   users_list.append(user)   ## This is the facking problem

#Post
@router.post("/",response_model=User,status_code=status.HTTP_201_CREATED)  # el parametro status_code sirve para reasignar un error talves por que es lo mejor # response-model es para poner el error en la documentacion
async def user(user:User):
  if type(search_user("email",user.email)) == User:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe")
    # Cuando lanzamos un error debe de ser con el raise
    
  user_dict = dict(user) # Entidad usario transformado en un usuario
  del user_dict["id"]
  id = db_client.local.users.insert_one(user_dict).inserted_id # Solo un registro

  new_user = user_schema(db_client.local.users.find_one({"_id":id}))
  return User(**new_user)

#Put

@router.put("/")
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


@router.delete("/{id}")
async def user(id: int):

  found = False

  for index, saved_user in enumerate(users_list):
    if  saved_user.id == id:
      del users_list[index]
      found = True
  if not found:
    return {"error": "no hay actualizacion"}


def search_user(field:str, key):

    try:
      user = db_client.local.users.find_one({field :key})
      return User(**user_schema(user))
    except:
      print("error")
      return {"error": "no hay usuario"}

# 6:52


#Path cuando los parametros son obligatorios
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
    # 500y superiores son para errores del servidor. Casi nunca los usas directamente. Cuando algo sale mal en alguna parte del código de su aplicación o servidor, automáticamente devolverá uno de estos códigos de estado\