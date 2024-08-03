"""Funciones que ponen nuevas funcionalidades a otras funciones
Por ejemplo: Tienes un mueble y le vas añadiendo cosas y una pared  y les vas añadiendo cuadros, lo que estas haciendo es decorar el mueble y cuadro respectivamente"""

#* Estructura
"""
- Son 3 funciones(A,B,C) donde A recibe como parametro a B para devolver C
- Un decorador devuelve una funcion"""
#* Ejemplo



"""
def suma():
  print(23+23)
def resta():
  print(32-12)
suma()
resta()"""

## Ahora queremos poner una funcionalidad de que antes y despues de hacer las operaciones diga un mensaje eso lo hacemos con un decorador

def funcion_decoradora(funcion_parametro): # una funcion que tiene como parametro otra funcion
  def funcion_interior(): #aqui deberiamos poner las nuevas funcionalidades y luego retornarlo
    # Acciones adicionales que decoran
    print("Vamos a realizar una calculo: ")
    funcion_parametro() ## Lo que normalmente hace la funcion a que estamos decorando
    # Acciones adicionales que decorar
    print("Hemos terminado el calculo")
  return funcion_interior


@funcion_decoradora # le decimos a  python que queremos decorar la funcion de abajo, y el decorador lo tomaria como el parametro de funcion_parametro, es decir la funcion_decoradora tomara a suma como parametro
def suma():
  print(23+23)
@funcion_decoradora # lo mismo con esto
def resta():
  print(32-12)
suma()
resta()