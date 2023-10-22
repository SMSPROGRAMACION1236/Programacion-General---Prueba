from fastapi  import FastAPI, Depends, HTTPException, status # Tipos de errores "status", puede ser mas visual 
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Se importa lo de la autenticacion  # IswordBearer, OAuth2PasswordRequestForm
##Autenticacion
# El sistema conoce al usuario, como el login
##Autorizacion
#Entrar en algo especifico como en el area de manejo de un canal.


app = FastAPI()

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
        "username" : 'sms',
        "full_name": "santiagosamnabria",
        "email" : "sanabriasanti1236@gmail.com",
        "disabled" : False,
        "password": "123456"
      },
      "santiago2": {
        "username" : 'sms2',
        "full_name": "santiagosamnabria 2",
        "email" : "sanabriasanti12326@gmail.com",
        "disabled" : True,
        "password": "654321"
      }
}


def search_user(username:str):
  if username in users_db:
    return UserDB(users_db[username])
  
async def current_user(token:str= Depends(oauth2)):
  user = search_user(token)
  if not user:
    raise HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticacion Invalidas", headers={"WWW-Authenticate":"Bearer"}) # Se recomienda usar el standar
  return user


  
  
# Depends traera datos y no depende de nada
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # El que caputura los datos
  user_db= users_db.get(form.username)
  if not user_db:
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Incorrect usuario")
  

  user = search_user(form.username)

  if not form.password == user.password:
     # Comprabar si el password coinicide con la base de datos
     raise HTTPException(
       status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
  
  return{"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user:User = Depends(current_user())):
  return user



# 4:40:37

# Debo tomar practicar
