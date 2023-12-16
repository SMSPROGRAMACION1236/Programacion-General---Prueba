
from pydantic import BaseModel # Nos da la capacidad de crear una entidad 
class User(BaseModel):
  id: str |None
  username : str
  email : str
