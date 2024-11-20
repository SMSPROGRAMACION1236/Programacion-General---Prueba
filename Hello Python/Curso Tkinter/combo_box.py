import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()
ventana.title("Ventana de ejemplo")
### Personalizacion

combobox = ttk.Combobox(ventana, width= 30, font=("Arial", 12), foreground="blue", background="white")
combobox.pack()
###  Creamo los elementos
elementos = ["Elemento 1", "Elemento 2", "Elemento 3"]
### Ponemos los elementos
combobox["values"] = elementos

## Si queremos eliminar algo, debemos de actualizar el combobox para que se guarde los datos
elementos.remove("Elemento 1") # Le pasamos el nombre del eleemnto
combobox["values"] = elementos  # Actualizamos los datos

#* Crear un evento

def on_selected(event):
  valor_seleccionado = combobox.get()
  print(f"Seleccionado: {valor_seleccionado}")
combobox.bind("<<ComboboxSelected>>", on_selected)

ventana.mainloop()