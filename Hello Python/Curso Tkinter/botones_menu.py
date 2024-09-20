import tkinter as tk

ventana = tk.Tk()


menubotton = tk.Menubutton(ventana, text="Archivo") # Le aplicamos ala ventana principal
menubotton.pack()

menu = tk.Menu(menubotton) # Creamoa el meno
menubotton.config(menu=menu) # le asociamos el meno que creamos


def abrir_archivo():
  print("Archivo Abierto")
def cerrar_archivo():
  print("Archivo Cerrado")

menu.add_command(label="Abrir", command=abrir_archivo) # Le asociamos la funcion abrir_archivo
menu.add_command(label="Cerrar", command=cerrar_archivo)


ventana.mainloop()