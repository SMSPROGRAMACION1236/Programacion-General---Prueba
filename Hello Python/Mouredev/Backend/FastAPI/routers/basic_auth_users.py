from fastapi  import FastAPI, Depends, HTTPException, status # Tipos de errores "status", puede ser mas visual 
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Se importa lo de la autenticacion  # IswordBearer, OAuth2PasswordRequestForm
##Autenticacion
# El sistema conoce al usuario, como el login
##Autorizacion
#Entrar en algo especifico como en el area de manejo de un canal.
from fastapi import APIRouter


router = APIRouter()# para conectar con el main y los demas APIs

oauth2 =  OAuth2PasswordBearer(tokenUrl="login")    # usamos la instancia, que nos dice como trabajar con autenticacion


class User(BaseModel):
  username : str
  full_name: str
  email : str
  disabled : bool
  

class UserDB(User):
  password: str

users_db = {
  "santiago": {
        "username": "SMS",  # Lo que se pasa al post es santiago no sms
        "full_name": "Franco Torres",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "123456"
    },
    "santiago2": {
        "username": "sms2",
        "full_name": "Franco Torres 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,  # Con esto si o si esta inactivo
        "password": "654321"
}
}


def search_user_db(username:str):
  if username in users_db:
    return UserDB(**users_db[username])
  

def search_user(username:str):
  if username in users_db:
    return User(**users_db[username])
  
# async def current_user(token:str= Depends(oauth2)):
async def current_user(token: str = Depends(oauth2)):
  user = search_user(token)
  if not user:
    raise HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticacion Invalidas",
        headers={"WWW-Authenticate": "Bearer"}) # Se recomienda usar el standar
  if user.disabled: # Lo puse de otro
         raise HTTPException(
             status_code=status.HTTP_400_BAD_REQUEST,
             detail="Usuario inactivo")
  return user


  
  
# Depends traera datos y no depende de nada
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # El que caputura los datos
  user_db= users_db.get(form.username)
  if not user_db:
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Incorrect usuario")
  

  user = search_user_db(form.username)

  if not form.password == user.password:
     # Comprabar si el password coinicide con la base de datos
     raise HTTPException(
       status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
  
  return{"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user:User = Depends(current_user)): # Por nada del mundo poner entre parentesis
  return user






# SQL es cuando se pueden relacionar con tablas, y se todos tienen conexiones
#No SQL no se relacionan, son documentos, tienen tipos de texto JSON, y se divide en directorios con documentos y se comportan de manera independiente, con esto ocupan poco y mas rapidas, y lo malo es el tema de relacionar NoSQL es cuando se puede tener una sola tabla


## pymongo es una libreria que te permite trabajar con la logica