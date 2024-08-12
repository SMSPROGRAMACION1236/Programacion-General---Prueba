class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  def  mostrar_datos(self):
    print(f"Nombre: { self.nombre} y tienes: {self.edad} años")

class Estudiante(Persona):
  def __init__(self, nombre, edad, curso):
    super().__init__(nombre, edad) # Cuando usamos super no usamos self
    self.curso = curso
  def mostrar_curso(self):
    print(f"Grado: {self.curso}")



estudiante = Estudiante('Juan', '13', '2do')
estudiante.mostrar_datos()
estudiante.mostrar_curso()
