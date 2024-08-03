"""Es una carpeta que tiene varios modulos
- Debe tener un archivo: __init__.py cual puede estar vacio, para que el interprete pueda identificar que es un packete
"""


def middle(numbs:list):
  count = 0
  for i in numbs:
    count += i
  return count/len(numbs)
    