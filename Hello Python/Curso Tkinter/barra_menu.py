import tkinter as tk

ventana = tk.Tk()

barra_menu = tk.Menu(ventana) # Le aplicamos el menu

ventana.config(menu=barra_menu)

archivo_menu = tk.Menu(barra_menu) # Le asociamos el menu
barra_menu.add_cascade(label="Archivo", menu=archivo_menu) # Le añadimos una cascada en forma de label, en el menu archivo_menu

#* Le podemos elementos

archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir")


editar_menu = tk.Menu(barra_menu)

barra_menu.add_cascade(label="Editar",menu=editar_menu)

help_menu = tk.Menu(barra_menu)

barra_menu.add_cascade(label="Help",menu=help_menu)


help_menu.add_command(label="Options")

#* Ponemos elementos

editar_menu.add_command(label="Deshacer")
editar_menu.add_command(label="Rehacer")
ventana.mainloop()