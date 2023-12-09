###Polimorfismo ###

"""
Es poder enviar un mensaje a varias clases, es el mismo mensaje para todos, pero con diferentes resultados, esto acontece por sus propiedades
El polimorfismo es una de las características más importantes del paradigma orientado a objetos. Se refiere al comportamiento común
Ejemplo:
Se le puede dar una orden de caminar a varios animales(que serian las otras clases) sim embargo cada tipo de animal tiene su propia forma de caminar
"""


class Gato:
  def sonido(self):
    return "Miau"
class Perro:
  def sonido(self):
    return "Guau"



def hacer_sonido(animal):
  print(animal.sonido())
gato = Gato()
perro = Perro()

hacer_sonido(gato)  # Misma funcion, diferente argumento, polimorfismo de funcion

# print(perro.sonido()) # Mismo metodo, cambia el objeto


#1:40:0