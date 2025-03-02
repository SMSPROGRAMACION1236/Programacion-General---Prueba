import tkinter as tk
from tkinter import filedialog
from icecream import ic


ventana = tk.Tk()

ventana.withdraw() # Ocultar ventana principal
#* Para solo un archivo a la vez
# file_path =  filedialog.askopenfilename() # Sirve para seleccionar un archivo y obtener su ruta absoluta
# ic(file_path)

#* Para muchos archivos a la vez
# files_path = filedialog.askopenfilenames() # Sirve para seleccionar varios archivos y obtener sus rutas absolutas
# ic(files_path)

#* Para abrir un archivo y leer su contenido
file_obj =  filedialog.askopenfile(mode="r")
if file_obj:
  ic(file_obj.read())
  file_obj.close()


# file_paths = filedialog.askopenfilenames()
# ic(file_paths)

# file_obj = filedialog.askopenfiles(mode="r")
# if file_obj:
#   ic(file_obj.read())
#   file_obj.close()

