class Empleado(Persona): # Para heredar en este caso Empleado herede los atributos de Persona simplemente debemos poner persona entre () 
  # pass # cuando creer algo pero no queremos definir que va a hacer`
  def __init__(self, name, age, country, work, salary): # Ponemos todos los atributos y los nuevos atributos
    super().__init__(name, age, country) # con super() te permite aclarar cuales atributos quieres heredar de la padre(Persona)
    self.trabajo = work
    self.salario = salary
  def hablar(self):
    print("no")