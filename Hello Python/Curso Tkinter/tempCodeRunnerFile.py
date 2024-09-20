from tkinter import Button, Tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename

def abrir_archivo():
  archivo = askopenfilename()
  if archivo:
    texto_desplazable.delete(1.0, "end")
    with open(archivo,"r") as file:
      texto_desplazable.insert(1.0, file.read())
      
def guardar_archivo():
  archivo = asksaveasfilename()
  if archivo:
    with open(archivo,"w") as file:
      file.write(texto_desplazable.get(1.0, "end"))
      
ventana = Tk()
