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
print("\tSeparador")# Para separar los prints
# para crear atributos de instancias
class Celular : # Cada vez que se crea un objeto, trabaja el contructor
  def __init__(self, marca, modelo, camera): # Esto es un constructo y defime las propiedades y self es como una forma de referirse a si mismo a un mismo objeto, en este caso a los parametros marca, modelo, y camara
    self.marca = marca # Es como decir celular.marca
    self.modelo = modelo
    self.camera = camera
    ### metodos ###
  def llamar(self):# Es importante ponerlo
      print(f"Estas llamando a alguien{self.modelo}")  # usamos el f string y le ponemos self.modelo o sea celular.modelo
  def cortar(self):
      print(f"Estas cortando desde un: {self.modelo}")

celular1 = Celular("Samsung", "S24", "48MP")# Es una funcion que se ejecuta siempre automaticamente cuando se crea un objeto
celular2 = Celular("Appe", "Iphone 15 pro", "32MP")# Es una funcion que se ejecuta siempre
celular3 = Celular("Huawei", "Mate40 pro", "64MP")# Es una funcion que se ejecuta siempre
print(celular1.marca)
print(celular2.marca)
print(celular3.marca)


celular2.llamar()

"""
Metodo = Accion
Atributo = Cualidad o caracteristica
"""

###Metodos ###

