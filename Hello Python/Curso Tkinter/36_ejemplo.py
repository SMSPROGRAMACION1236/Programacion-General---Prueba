import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
  file_path = filedialog.askopenfilename(filetypes=[('Archivo de texto', '*.txt'), ('Todos los archivos', '*.*')]) # Explicacion: Sirve para seleccionar un archivo y obtener su ruta absoluta y se puede filtrar por extensiones de archivo (filetypes=[('Archivo de texto', '*.txt'), ('Todos los archivos', '*.*')])
  
  if file_path:
    with open(file_path, "r") as file_obj: # Explicacion: Abre el archivo en modo lectura y se cierra automaticamente al finalizar el bloque de codigo con la sentencia with open() as file_obj:
      contenido = file_obj.read() # Explicacion: Lee el contenido del archivo y lo guarda en la variable contenido
      text_widget.delete(1.0, tk.END) # Explicacion: Borra el contenido actual del widget de texto
      text_widget.insert(tk.END, contenido) # Explicacion: Inserta el contenido del archivo en el widget de texto


ventana = tk.Tk()
ventana.title("Visor de archivos de Texto")

text_widget = tk.Text(ventana, wrap="word") # Explicacion: Crea un widget de texto con ajuste de linea
text_widget.pack(expand=True, fill="both") # Explicacion: Empaqueta el widget de texto en la ventana

abrir_boton = tk.Button(ventana, text="Abrir archivo", command=abrir_archivo) # Explicacion: Crea un boton para abrir un archivo y llama a la funcion abrir_archivo() cuando se presiona
abrir_boton.pack()

ventana.mainloop()