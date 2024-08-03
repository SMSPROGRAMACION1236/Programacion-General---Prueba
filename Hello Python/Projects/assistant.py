import webbrowser # Nos sirve para abrir el navegador web
import pyttsx3 #  Para la conversacion de texto a voz
import  speech_recognition as sr # para el reconocimiento de voz.

recognizer = sr.Recognizer() # Se crea el objeto de la biblioteca speech_recognition

engine = pyttsx3.init() # Se inicializa un motor de texto a voz usando pyttsx3.


def talk():
  mic = sr.Microphone() # . Inicializa un micrófono usando speech_recognition.
  with mic as source:
    audio = recognizer.listen(source) # Escucha la entrada de voz del usuario usando el método listen() del objeto Recognizer.
  text = recognizer.recognize_google(audio, language="ES") # Convierte la entrada de voz en texto usando el método recognize_google() del objeto Recognizer.
  
  print(f"Has hecho: {text}") #Imprime el texto reconocido.
  return text.lower() #  Devuelve el texto reconocido en minúsculas.
if 'amazon' in talk(): #Se llama a la función talk(). Si el texto reconocido contiene la palabra 'amazon', el motor de texto a voz dice "Que productos quieres : " .
  engine.say("Que producto quieres : ")
  engine.runAndWait()  # lo ejecuta o espera
  text = talk()
  webbrowser.open(f"https://www.amazon.es/s?k={text}") # y luego abre el sitio web de Amazon España con la consulta del usuario
    