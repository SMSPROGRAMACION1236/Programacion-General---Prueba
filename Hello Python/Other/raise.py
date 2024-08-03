
#! Tiny int
""" Crearemos una excepcion para tiny int
0 al 255
Positivo"""
#* Que es
""" Es para lanzar de forma explicita una excepcion"""

class TinyIntError(Exception): #* Para usar el raise debemos de heredar el Exception y reconozca como error(si es que queremos crear una excepcion personalizada.)
  pass
def tiny_int(val):
  return val >= 0 and val <= 225
try:
  numero = 2232

  if tiny_int(numero):
    print("El numero es correcto")
  else:
    raise TinyIntError("No es posible completar la operacion")

except TinyIntError as error:
  print(error)
  
  
#! Ejemplo Mine:
def exception(a,b):
  if b == 0:
    raise ZeroDivisionError("No se puede dividir entre 0")
  else:
    return a/b
    
try:
  result = exception(2,0)
  print(result)
except ZeroDivisionError as error:
  print(error)
  