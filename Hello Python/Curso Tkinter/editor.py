from tkinter import Button, Tk
from tkinter.scrolledtext import ScrolledText  # Te permite  hacer el scroll
from tkinter.filedialog import askopenfilename, asksaveasfilename # Te permite guardar  y abrir archivos

def abrir_archivo():
  archivo = askopenfilename() # abrir el archivo
  if archivo:
    texto_desplazable.delete(1.0, "end") #  Se borra todo lo que estaba en el texto desplazable
    with open(archivo,"r") as file:
      texto_desplazable.insert(1.0, file.read()) # se insertar lo que esta en el archivo
      
def guardar_archivo():
  archivo = asksaveasfilename() # guardar el archivo
  if archivo:
    with open(archivo,"w") as file:
      file.write(texto_desplazable.get(1.0, "end")) # Guardar todo lo que esta en el texto desplazable
      
ventana = Tk()

texto_desplazable = ScrolledText(ventana, wrap="word") # se cortara por palabra 
texto_desplazable.pack(expand=True,fill="both") # se puede expandir, y se llenara de ambos lados

boton_abrir = Button(ventana, text="Abrir", command= abrir_archivo)
boton_abrir.pack(side="left")

boton_guardar = Button(ventana, text="Guardar", command= guardar_archivo)
boton_guardar.pack(side="left")

ventana.mainloop()