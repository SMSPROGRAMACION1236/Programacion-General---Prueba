
from pydantic import BaseModel # Nos da la capacidad de crear una entidad 

from typing import Optional
class User(BaseModel):
  id: Optional[str] # To be optional
  username : str
  email : str
