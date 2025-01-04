import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana de ejemplo")
### Personalizacion
list_box = tk.Listbox(ventana, width=30, height= 10, font=("Arial", 12), fg="blue", bg="white") # Aqui podremos poner el selectmode = tk. MULTIPLE para que podamos seleccionar mas de una opcion

### Ponemos los elementos
list_box.insert(tk.END, "Elemento 1") # tk.END es para poner las cosas al final
list_box.insert(tk.END, "Elemento 2")
list_box.insert(tk.END, "Elemento 3")


### Para eliminar elementos
list_box.delete(0) # Eliminamos el elemento del indice 0, en este caso elemento 1
#* Podemos crear eventos tambien
def on_selected(event):
  indice = list_box.curselection() # Obtener el indice el elemento seleccionado
  elemento = list_box.get(indice) # Obtener el elemento apartir del indice
  print(f"Seleccionado: {elemento}")
list_box.bind('<<ListboxSelect>>', on_selected)

list_box.pack()
ventana.mainloop()

