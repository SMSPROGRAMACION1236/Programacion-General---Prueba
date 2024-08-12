from fastapi  import FastAPI, Depends, HTTPException, status # Tipos de errores "status", puede ser mas visual 
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Se importa lo de la autenticacion  

from jose import jwt, JWTError  # Este es  nuevo modulo
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
SECRET ="201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b" # "3d201d372020c009416c1ddf9713ef7576bdf08351fabcda1c58a4432885d865"


app = FastAPI()

oauth2 =  OAuth2PasswordBearer(tokenUrl="login")    # usamos la instancia, que nos dice como trabajar con autenticacion

crypt =  CryptContext(schemes=["bcrypt"]) # Algoritmo de encriptacion


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

def search_user_db(username: str):
  if username in users_db:
    return UserDB(**users_db[username])
  

def search_user(username: str):
  if username in users_db:
    return User(**users_db[username]) # Busca el usuario de la base de datos
  
# con esto podremos llamar a la variable exception y asi no repetir codigo
 # Se recomienda usar el standar
async def auth_user(token: str = Depends(oauth2)):
    

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        
        
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
           detail="Usuario inactivo")
    return user
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password): # para verificar si el password es correcto
     # Comprabar si el password coinicide con la base de datos
        raise HTTPException(
       status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
  

#  timedelta(minutes=ACCESS_TOKEN_DURATION) # Crea un delta de un minuto mas de lo que tenemos y luego lo sumamos con el tiempo de ahora 
    access_token = {"sub":user.username,
                    "exp": datetime.utcnow() +  timedelta(minutes=ACCESS_TOKEN_DURATION)}
# Con jwt lo encriptamos y luego le pasamos el algoritmo
    return{"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

# Por nada del mundo poner entre parentesis
@app.get("/users/me/")
async def me(user: User = Depends(current_user)):
    return user

#Para comprobar si el "access_token" encriptado coincide con el username y los demas datos  https://jwt.io/ puedes usar esto 

# Puedes usar https://bcrypt-generator.com/ para encriptar contrasenas 



## La documentacion en donde me quede https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation