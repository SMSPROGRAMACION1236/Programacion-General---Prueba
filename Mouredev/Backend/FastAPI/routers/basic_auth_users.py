from fastapi  import FastAPI, Depends, HTTPException
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
  

# Depends traera datos y no depende de nada
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): # El que caputura los datos
  user_db= users_db.get(form.username)
  if not user_db:
    raise HTTPException(status_code=400, detail="Incorrect usuario")
  

  user = search_user(form.username)

  if not form.password == user.password:
     # Comprabar si el password coinicide con la base de datos
     raise HTTPException(
       status_code=400, detail="Incorrect password")
  
  return{"access_token": user.username, "token_type": "bearer"}

