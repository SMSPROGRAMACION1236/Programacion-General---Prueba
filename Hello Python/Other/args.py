### Sirve para poner mas argumentos de los que fueron creados, es decir recibir un numero arbitrario de argumentos
def suma(a,b):
  return a+b
print(suma(23,32,32)) #!error


#* para poder hacer esto, podemos poner tupla, usando el * ( normalemente se usa args, pero se puede llamar como tu quieres)
## Los argumentos que no fueron definidos o indicados, se iran acumulando en una tupla

def suma(a,b,*args): ## en este caso minimo dos argumentos debemos pasarle, y los demas ya es opcion cual se va acumulando en la tupla
  print(type(args))
  return a+b+sum(args)
print(suma(23,32,123,32))