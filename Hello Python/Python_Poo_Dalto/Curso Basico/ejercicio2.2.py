class Animal:
  def comer(self):
    print("Comiendo")
class Ave(Animal):
  def volar(self):
    print("Volando")
class Manifero(Animal):
  def amamantar(self):
    print("amamantando")


class Murcielago(Manifero, Ave):
  pass

murci = Murcielago()

murci.comer()
murci.amamantar()
murci.volar()


print(Murcielago.mro()) # Para saber el orden de ejecucion 