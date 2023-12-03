# /*

#  * Escribe un programa que reciba un texto y transforme lenguaje natural a

#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje

#  *  se caracteriza por sustituir caracteres alfanuméricos.

#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 

#  *   con el alfabeto y los números en "leet".

#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

#  *

#https://retosdeprogramacion.com/semanales2023



def leet_speak(text): # El diccionario se almacenara aqui 
  resultado = "" # Donde almacenaremos el resultado\
  #El diccionario de clave y valor
  diccionario ={ 

    "A": "4",

    "B": "13",

    "C": "[",

    "D": ")",

    "E": "3",

    "F": "|=",

    "G": "&",

    "H": "#",

    "I": "1",

    "J": ",_|",

    "K": ">|",

    "L": "1",

    "M": "/\/\\",

    "N": "^/",

    "O": "0",

    "P": "|*",

    "Q": "(_,)",

    "R": "|2",

    "S": "5",

    "T": "7",

    "U": "(_)",

    "V": "\/",

    "W": "\/\/",

    "X": "><",

    "Y": "j",

    "Z": "2"

  }
  
  text = text.upper()  # transformar todo el string en mayuscula
  
  for letra in text:
    if letra  in diccionario: # si la letra esta en el diccionario
      resultado += diccionario[letra]
    else: #si no esta
        resultado += letra
  return resultado



print(leet_speak(str(input("Ingrese una palabra: "))))


