###Polimorfismo ###

"""
Es poder enviar un mensaje a varias clases, es el mismo mensaje para todos, pero con diferentes resultados, esto acontece por sus propiedades
El polimorfismo es una de las características más importantes del paradigma orientado a objetos. Se refiere al comportamiento común
Ejemplo:
Se le puede dar una orden de caminar a varios animales(que serian las otras clases) sim embargo cada tipo de animal tiene su propia forma de caminar
"""


class Cat:
  def sound(self):
    return "Miau"
class Dog:
  def sound(self):
    return "Guau"



def make_sound(animal):
  print(animal.sound())
cat = Cat()
dog = Dog()

make_sound(cat)  # Misma funcion, diferente argumento, polimorfismo de funcion

# print(dog.sound()) # Mismo metodo, cambia el objeto


print("\t Polimorfismo de coaccion")


num1 = 3
num2 =  4.4

result = num1 + num2

print(result)
print(type(num1))
print(type(num2))
print(type(result))


#TODO:Duck Typing, Enlaces dinamicos, estaticos, tipo real, o tipo declarado

"""El duck typing o tipado pato es un estilo de tipificación dinámica de datos que se usa en algunos lenguajes de programación orientados a objetos. En el duck typing, lo que importa es el comportamiento de los objetos, no su tipo."""

"""El enlace dinámico y el enlace estático son dos técnicas de programación que se refieren a la forma en que se resuelven las llamadas a funciones o métodos en tiempo de ejecución. El enlace dinámico ocurre cuando el objeto al que se llama una función no se conoce hasta que se ejecuta el programa, mientras que el enlace estático ocurre cuando el objeto se conoce en el momento de la compilación. El enlace dinámico permite una mayor flexibilidad y polimorfismo, pero también implica un mayor costo de rendimiento y memoria. El enlace estático, por el contrario, es más rápido y eficiente, pero también más rígido y propenso a errores de compatibilidad"""

"""Un tipo real o tipo dinámico de un objeto es el tipo de la clase a la que pertenece realmente el objeto en tiempo de ejecución. Por ejemplo, si tenemos una clase Animal y una clase Perro que hereda de Animal, y creamos un objeto de tipo Perro, su tipo real será Perro, aunque también se pueda considerar como un Animal. Un tipo declarado o tipo estático de un objeto es el tipo de la variable que se usa para referenciar al objeto en tiempo de compilación."""
