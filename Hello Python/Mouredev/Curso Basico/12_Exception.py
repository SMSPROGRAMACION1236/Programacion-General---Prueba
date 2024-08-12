### Exceptions ###
""" Bloques para manejar errores"""
numberOne, numberTwo = 5, 1

numberTwo = "1"
# Para saber si existe un error osea para poder controlarlo

## try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido el error")  # Se ejecuta si hay una exception
##try except else
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido el error")
else: # Opcional
    print("La ejecucion continua")  # Se ejecuta si el try esta bien, continua el try

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido el error")
else:
    print("La ejecucion continua")
finally: # Opcional
    print("Sigue en funcion")  # Se ejecuta siempre se ejecuta

## Exceptiones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError :
    print("Se ha producido un ValueError")
except TypeError:  # Se ejecuta esta clase de error
    print("Se ha producido el TypeError")
## Captura de la informacion de la excepcion.
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:  # Para guardar la informacion de un error en una  variable
    print(error)
except Exception as wasaa:
    print(wasaa)