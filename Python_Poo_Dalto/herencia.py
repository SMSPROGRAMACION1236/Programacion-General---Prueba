### Herencia###
#La herencia es heredar atributos, por ejemplo una clase hija de una clase padre, es decir la hija hereda los atributos de la clase padre, pero la hija puede tener mas atributos, en resumen es reutilizar codigo


class Persona :
  def __init__(self, name, age, country):
    self.nombre = name
    self.edad = age
    self.nacionalidad = country
  def hablar(self):
    print("Estoy hablando")


class Empleado(Persona): # Para heredar en este caso Empleado herede los atributos de Persona simplemente debemos poner persona entre () 
  # pass # cuando creer algo pero no queremos definir que va a hacer`
  def __init__(self, name, age, country, work, salary): # Ponemos todos los atributos y los nuevos atributos
    super().__init__(name, age, country) # con super() te permite aclarar cuales atributos quieres heredar de la padre(Persona)
    self.trabajo = work
    self.salario = salary
class Estudiante(Persona): # Para heredar en este caso Empleado herede los atributos de Persona simplemente debemos poner persona entre () 
  # pass # cuando creer algo pero no queremos definir que va a hacer`
  def __init__(self, name, age, country, notas, colegio): # Ponemos todos los atributos y los nuevos atributos
    super().__init__(name, age, country) # con super() te permite aclarar cuales atributos quieres heredar de la padre(Persona)
    self.trabajo = notas
    self.salario = colegio
  
roberto = Empleado("Roberto", 23, "Paraguayo", "Dev", "110023")
roberto.hablar()


"""

herencia simple: Cuando solo hay una clase padre y una hija
herencia jerarquica: cuando hay una clase padre y sus hijos, cuales dependen del padre"""