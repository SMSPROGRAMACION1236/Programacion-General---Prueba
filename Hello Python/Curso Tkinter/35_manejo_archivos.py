import tkinter as tk
from tkinter import filedialog


ventana = tk.Tk() 
ventana.withdraw()  # Ocultar ventana principal
#* Forma 1
file_path = tk.filedialog.askopenfilename()  # Seleccionar un archivo y obtener su ruta absoluta
print(file_path)  # Mostrar la ruta del archivo seleccionado

#* Forma 2
files_path = filedialog.askopenfilenames()  # Seleccionar varios archivos y obtener sus rutas absolutas
print(files_path)

#* Forma 3
file_obj = filedialog.askopenfile(mode="r")  # Abrir un archivo y leer su contenido
if file_obj:
    print(file_obj.read())  # Leer el contenido del archivo
    file_obj.close()  # Cerrar el archivo