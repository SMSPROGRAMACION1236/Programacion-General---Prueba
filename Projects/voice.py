import webbrowser
import pyttsx3
import  speech_recognition as sr

recognizer = sr.Recognizer()

engine = pyttsx3.init()


def talk():
  mic = sr.Microphone()
  with mic as source:
    audio = recognizer.listen(source)
  text = recognizer.recognize_google(audio, language="ES")
  
  print(f"Has hecho: {text}")
  return text.lower()
if 'amazon' in talk():
  engine.say("Wasaaaa : ")
  engine.runAndWait()
  text = talk()
  webbrowser.open(f"https://www.amazon.es/s?k={text}")
    