# Es cuando podemos agregar mas valores, sin embargo en situaciones donde cada valor pasado a la funcion, este asociado con cierta clave, cada uno, no es recomendable args
#* Se usa un diccionario, para poner los claves| valor
""" Normalmente se llama kargs pero puede llamarse como quieras
    Debe tener el ** antes del nombre que usaras
"""
#! Forma mala
def expediente(historia, mates, lengua):
  print("historia", historia)
  print("mates", mates)
  print("lengua", lengua)
  media = historia + mates + lengua 
  print("media", media /3)
expediente(3,4,5)

#! Forma buena
def buen_expendiente(**kargs):
  media = 0
  for i in kargs:
    print(f"{i}: {kargs[i]}")
    media += kargs[i]
  return f"La media es: {media / len(kargs)}"
## Por lo que a la funcion, podemos pasarle las materias y sus valores sin ninguna limitacion
print(buen_expendiente(historia=3, mates=4, lengua=5))
#* Se puede mezclar otros tipos como args, posicionales  o por nombres, etc o todo una mezcla o todo.
"""
Reglas:
- Primero posicionales
- Luego args
- Por nombres
- Kargs
"""