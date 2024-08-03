#Este es un script de Python que establece una alarma

print(os)
import os ##Esta línea importa el módulo os, que proporciona una forma de utilizar la funcionalidad dependiente del sistema operativo.

import time ## Esta línea importa el módulo time, que proporciona varias funciones relacionadas con el tiempo.
from playsound import playsound# Esta línea importa la función playsound del módulo playsound, que se puede usar para reproducir sonidos.
def alarm(minutes, seconds): # Esta línea define una función llamada alarm que toma dos argumentos: minutes y seconds.
  sound_path =os.path.join( os.path.dirname(__file__), "serious-dark-ambient-atmosphere.mp3")# Esta línea establece la ruta al archivo de sonido que se reproducirá cuando suene la alarma. La función os.path.join se utiliza para unir el directorio del archivo actual y el nombre del archivo de sonido en una sola ruta.
  total_seconds= minutes * 60 + seconds # Esta línea calcula el número total de segundos para la alarma multiplicando el número de minutos por 60 y sumando el número de segundos.
  print(f"La alarma sonara en {minutes} y {seconds} segundos") #Esta línea imprime un mensaje en la consola indicando cuándo sonará la alarma.
  time.sleep(total_seconds) # Esta línea hace que el programa se detenga durante el número total de segundos calculados anteriormente.
  playsound(sound_path) # Esta línea reproduce el archivo de sonido en la ruta especificada anteriormente.
  
minutes = int(input("Ingresa los minutos de la alarma: "))#Esta línea pide al usuario que ingrese el número de minutos para la alarma y convierte la entrada en un entero.

seconds = int(input("Ingresa los segundos de la alarma: "))# Esta línea pide al usuario que ingrese el número de segundos para la alarma y convierte la entrada en un entero.
alarm(minutes, seconds) #Esta línea llama a la función alarm con el número de minutos y segundos ingresados por el usuario.