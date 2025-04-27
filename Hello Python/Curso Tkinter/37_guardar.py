from tkinter import filedialog 
import tkinter as tk


ventana = tk.Tk()

ventana.withdraw() # Ocultar ventana principal

file_obj = filedialog.asksaveasfile(mode="w", defaultextension= ".txt") # Abre un cuadro de dialogo para guardar un archivo y devuelve un objeto de archivo y el modo de apertura es "w" (escritura) y el nombre por defecto es ".txt"
if file_obj:
  file_obj.write("Hola Mundo") # Escribe "Hola Mundo" en e l  archivo
  file_obj.close() # Cierra el archivo
  
  
  