### MRO(Metodo de Resolucion de Orden) ###
# Es el metodo que busca cual clase o metodo ejecutara, o sea por prioridad\



class A:
  def hablar(self):
    print("Hola desde: A")
class F:
  def hablar(self):
    print("Hola desde: F")
class B(A):
  # def hablar(self):
  #   print("Hola desde: B")
  pass
  
class C(F):
  def hablar(self):
    print("Hola desde: C")
  
class D(B, C):
  # def hablar(self):
  #   print("Hola desde: D")
  pass  

d = D()
d.hablar() # la orden de ejecucion es D, ya que literalmente d = D, luego es B y C ya que estos estan indirectamente heredadas como subclase, y por ultimo A, es decir D>B>C>A y si agregamos otra clase F, el orden es D>B>A>C>F