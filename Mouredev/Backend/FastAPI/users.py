from fastapi import FastAPI 
from pydantic import BaseModel # Nos da la capacidad de crear una entidad 

app = FastAPI()

@app.get("/usersjson")
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


@app.get("/users")
async def users():
  return users_list


#Parh
@app.get("/user/{id}")
async def user(id: int):
  users =  filter (lambda user: user.id == id, users_list)
 
 

# No se puede poner id 4 ya no existe
  try:
    return list(users)[0]
  except:
    return {"error": "no hay usuario"} # En los casos de sea 4 y asi explica el error
  
#Query

@app.get("/userquery/")
async def user(id: int, name:str): # Si hay mas parametros en el navegador se debe de especificar eso con el & luego el parametro y el valor
  users =  filter (lambda user: user.id == id, users_list)
  return search_user(id)
#query podemos igualar una clave con un valor en una url en donde debemos de tipar todo y usa el signo ?
@app.post("/user/")
async def user(user:User):
  users_list.append(user)




#Post
@app.post("/user/")
async def user(user:User):
  if type(search_user(user.id)) == User:
    return {"error": "hay usuario"}
  else:
    users_list.append(user)  # En el cliente en la parte de json debemos de poner los datos 

#Put

# @app.put("/user/")
# async def user(user:User):
  #Aqui  me quede debo de insistir en no perder tanto tiempo


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
# DELETE: para borrar datos.




