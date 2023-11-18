# celular1_marca = "Samsung"
# celular2_marca = "Apple"
# celular3_marca = "Huawei"

# celular1_modelo = "S23"
# celular2_modelo = "Iphone 15 pro"
# celular3_modelo = "p20 Pro"

# celular1_camaraT = "48 MP"
# celular2_camaraT = "48 MP"
# celular3_camaraT = "12 MP"

# celular1_camaraF = "24 MP"
# celular2_camaraF = "24 MP"
# celular3_camaraF = "8 MP"
# print(celular1_marca) # Esto es una mala practica


# celulares = []

# celulares[1]= ["samsung", "s24", "..."] # Es una mala practica



###Class###

  # Se recomienda usar pascal case primeras letras en mayusculas todos
  
class NombreClase():  # Este es el modelo
  propiedad1 = "Valor 1"
  propiedad2 = "Valor 2"
  propiedad3 = "Valor 3"
# Un objeto es una instancia de una clase
# Esto es fijo
class Phone():
  marca = "Samsung"
  modelo = "S23"  # #Estos son atributos( Es como una propiedad)
  camera = "48MP"

celular1 = Phone() # El objeto celular1 es instancia de Celular

print(celular1) # Te dice que es un objeto y donde se almacena en la ram
# Estos son atributos estaticos podemos cambiar el valor pero no otro atributo

print(celular1.marca) # Algo especifico
print(celular1.camera)
print(celular1.modelo)


### ATRIBUTOS ###

# print(marca) No hay por que debemos poner primero la clase

celular1.marca = 'Apple'

print(celular1.marca) # Ahi lo cambiamos pero no es una buena practica


class Celular :
  def __init__(self) -> None: # Esto es un constructor, cad
    pass

27:04