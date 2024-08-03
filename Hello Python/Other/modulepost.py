### formas de usar funcionalidades de otros archivos
## Al hacer esto, genera una carpeta donde se guarda la compilacion
"""
Importamos el archivo:
Que se encuentra en la misma ruta, es decir modulepre y modulepost estan en la mimsa ruta"""

import Other.modulepre as modulepre ## tras importarlo, podemos acceder a las funcionalidades del fichero, con un punto

print(modulepre.division(1,1))

""" Traer cosas especificas, con el from ponemos el fichero y el import especificamos que queremos traer entre comas o con el "*" es para traer todo
  """

from Other.modulepre import multiplicacion, division, variable # variable es una variable como dice su nombre

print(multiplicacion(23,2))
#* Podemos traer variables 
print(variable)