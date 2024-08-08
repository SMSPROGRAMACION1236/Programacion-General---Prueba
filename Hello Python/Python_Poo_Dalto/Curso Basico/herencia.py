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
herencia jerarquica: cuando hay una clase padre y sus hijos, cuales dependen del padre
Herencia Multiple: Es cuando una clase puede heredar 2 o mas clases"""

class Artista:
  def __init__(self, habilidad_artistica):
    self.habilidades_artisticas = habilidad_artistica
  def mostrar_habilidad(self):
    return f"Mi habilidad es: {self.habilidades_artisticas}"


class EmpleadoArtista(Persona, Artista):
  def __init__(self, name, age, country, habilidad_artistica,salario:int , company):
    Persona.__init__(self, name, age, country) # Especificamos de que clase queremos heredar y poner como parametros los atributos
    Artista.__init__(self, habilidad_artistica)# Especificamos de que clase queremos heredar y poner como parametros los atributos
    self.salario = salario #Esto es lo nuevo
    self.company = company# eso es lo nuevo
  def presentarse(self):
    # return f"{super().mostrar_habilidad()}" # le decimos al programa que mostrar_habilidad es un metodo que estamos trayendo desde arriba(no es self, sino que es una heredacion) con esto siempre accedes a la clase padre
    print(f"Hola soy: {self.nombre},y {self.mostrar_habilidad()} y trabajo en{self.company}y gano: {self.salario}") #Es lo mismo que el de arriba

# Buenas Practica
"""
super : Cuando quieres llamar a clase padre
self : Cuando quieres llamar el de la misma clase

"""
# Investigar return vs print

roberto = EmpleadoArtista("Roberto", 23, "Paraguayo","Cantar", 110023, "Amazon")
roberto.presentarse()


herencia_proof = issubclass(EmpleadoArtista, Artista)# Te permite sabe si EmpleadoArtista es subclase de Artist
print(herencia_proof)
instancia = isinstance(roberto, EmpleadoArtista) # para saber si una variable es una instancia de una clase, es true ya que roberto es un objeto de la clase EmpleadoArtista
print(instancia)




