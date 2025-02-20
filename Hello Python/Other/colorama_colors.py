from colorama import init, Fore, Back, Style

init()

def font():
  print(Fore.RED + "Hola Mundo" + Style.RESET_ALL) # Color de Fuente y RESET ALL para que lo siguiente sea lo normal
  print("Wasaaa")
font()


def back():
  print(Back.RED + "Hola" + Style.RESET_ALL) # Color de Fondo
back()
  
def style():
  print(Style.BRIGHT + "Hola Mundo")  # Estilo de Fuente
style()

def mix():
  print(Style.DIM + Back.MAGENTA + Fore.BLACK + "Hola Mundo Soy un Insano" + Style.RESET_ALL) # Varios a la vez
  print(Fore.BLUE + "Hola" + Fore.RED + " Mundo" + Style.RESET_ALL)
mix()
