from fastapi  import FastAPI, Depends, HTTPException, status # Tipos de errores "status", puede ser mas visual 
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Se importa lo de la autenticacion  

from jose import jwt  # Este es  nuevo modulo
# IswordBearer, OAuth2PasswordRequestForm
##Autenticacion
# El sistema conoce al usuario, como el login
##Autorizacion
#Entrar en algo especifico como en el area de manejo de un canal.

from passlib.context import CryptContext

from datetime import datetime, timedelta  # Para calcular la fecha en la duracion del token y los calculos

ALGORITHM  = "HS256"  # Con esto podremos encriptar la password

ACCESS_TOKEN_DURATION = 1 # 1 minuto seria la duracion del token
 # Con esto puedes hacerlo mas seguro ya que tendra una clave que solo el backend lo conoce es una forma de encriptar el usuario de retorno
 ### Puede usar openssl rand -hex 32 en la terminal y te generara una clave secreta  de forma ramdon
SECRET = "3d201d372020c009416c1ddf9713ef7576bdf08351fabcda1c58a4432885d865"


app = FastAPI()

oauth2 =  OAuth2PasswordBearer(tokenUrl="login")    # usamos la instancia, que nos dice como trabajar con autenticacion

crypt =  CryptContext(schemes="bcrypt") # Algoritmo de encriptacion


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
        "password": "$2a$12$zDQR814zZ331FNwZMGWEt.uuSOcPVNQDSUTm1AUvDBucwZA9TCuU2"
    },
    "santiago2": {
        "username": "sms2",
        "full_name": "Franco Torres 2",
        "email": "braismoure2@mourede.com",
        "disabled": True,  # Con esto si o si esta inactivo
        "password": "$2a$12$vec3y6SYo1VRD.soG3WavOC/vGqXRKvNvXqU40JZTAAErk.Kz/3Me "
}
}

def search_user_db(username:str):
  if username in users_db:
    return UserDB(**users_db[username])
  

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # El que caputura los datos
  user_db= users_db.get(form.username)
  if not user_db:
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Incorrect usuario")
  

  user = search_user_db(form.username)


  

  if not crypt.verify(form.password, user.password): # para verificar si el password es correcto
     # Comprabar si el password coinicide con la base de datos
     raise HTTPException(
       status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
  

#  timedelta(minutes=ACCESS_TOKEN_DURATION) # Crea un delta de un minuto mas de lo que tenemos y luego lo sumamos con el tiempo de ahora 
  access_token = {"sub":user.username,
                  "exp": datetime.utcnow() +  timedelta(minutes=ACCESS_TOKEN_DURATION)}
# Con jwt lo encriptamos y luego le pasamos el algoritmo
  return{"access_token": jwt.encode(access_token,SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


#Para comprobar si el "access_token" encriptado coincide con el username y los demas datos  https://jwt.io/ puedes usar esto 

# Puedes usar https://bcrypt-generator.com/ para encriptar contrasenas 



## La documentacion en donde me quede https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation