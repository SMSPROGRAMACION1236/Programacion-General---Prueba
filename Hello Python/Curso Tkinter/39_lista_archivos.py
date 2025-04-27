import tkinter as tk
from tkinter import filedialog
import os

def seleccionar_directorio():
  dir_path = filedialog.askdirectory()  # Seleccionar un directorio y obtener su ruta absoluta
  if dir_path:
    list_box.delete(0, tk.END)  # Limpiar la lista antes de mostrar los archivos
    for archivo in os.listdir(dir_path):
      list_box.insert(tk.END, archivo)


ventana = tk.Tk()
ventana.title("Navegador de Archivos")


list_box = tk.Listbox(ventana)  # Crear un Listbox para mostrar los archivos
list_box.pack(expand=True, fill="both")  # Empaquetar el Listbox en la ventana


seleccionar_button = tk.Button(ventana, text="Seleccionar Directorio", command=seleccionar_directorio)  # Crear un botón para seleccionar un directorio
seleccionar_button.pack()  # Empaquetar el botón en la ventana

ventana.mainloop()  # Iniciar el bucle principal de la ventana
