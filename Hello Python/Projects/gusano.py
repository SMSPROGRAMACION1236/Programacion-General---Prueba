# primer argumento es el archivo y el segundo el numero de copias['gusano.py,'2']


import  shutil #Esta línea importa el módulo shutil, que proporciona una interfaz de nivel superior al trabajar con archivos.
import sys # Esta línea importa el módulo sys, que proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python y a funciones que interactúan fuertemente con el intérprete.

if len(sys.argv) ==2: # Esta línea verifica si el número de argumentos de línea de comandos pasados al script es igual a 2. Si es así, el script procederá a copiar el archivo. Si no, imprimirá un mensaje de error.


  for  num in range(0, int(sys.argv[1])) :# Esta línea crea un bucle que se ejecuta un número especificado de veces. El número de veces que se ejecuta el bucle está determinado por el primer argumento de línea de comandos pasado al script.
    shutil.copy(sys.argv[0], sys.argv[0]+f"{num}.py") # Esta línea copia el archivo especificado por el primer argumento de línea de comandos a un nuevo archivo con un nombre que incluye el número de iteración del bucle actual.
else:
  print("Envia dos parametros")