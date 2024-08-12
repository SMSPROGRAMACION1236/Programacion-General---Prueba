class Estudiante():
  def __init__(self, nombre, edad, grado) -> None:
    self.nombre = nombre
    self.edad = edad
    self.grado = grado
  def estudiar(self):
    print("estudiando...")

nombre = input("su nombre: ")
edad = int(input("tu edad: "))
grado = int(input("tu grado: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE:\n\n
      Nombre: {estudiante.nombre}\n
      Edad : {estudiante.edad}\n
      Grado: {estudiante.grado}\n

""")
while True:
  estudiar = input()
  #Lo ponemos en minusculas
  if(estudiar.lower() == "estudiar"):
    estudiante.estudiar()