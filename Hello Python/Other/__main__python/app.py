"wasaa"
"""Controla como se comporta nuestro archivo, cuando un archivo se ejecuta directamete o como modulo"""



print(__name__) ## Retorna main, en caso de que este archivo lo usemos en otro, entonces retornara el nombre de este archivo, si ejecutamos el otro archivo una vex importado el de app



def funcion_principaL():
  print("Esta es la funcion principal")
  
def funcion_auxiliar():
  print("esta funcion se podria usar al importar este archivo")
  
  
if __name__ == '__main__':
  funcion_principaL()