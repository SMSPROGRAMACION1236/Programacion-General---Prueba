
#* Utilidad
""" Sirve para crear un menu de acceso rapido por ejemplo el menu que aparece al hacer clic derecho, etc"""
import tkinter as tk

ventana = tk.Tk()

def mostrar_menu_contexual(event):
  menu_contextual.tk_popup(event.x_root, event.y_root)
#* Elementos del Menu
menu_contextual = tk.Menu(ventana, tearoff=0) # el tearoff te permite separar el menu, cuando es 0 no te permite
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label ="Copiar")
menu_contextual.add_command(label ="Cortar")

entrada = tk.Entry(ventana)
entrada.pack()


entrada.bind("<Button-3>", mostrar_menu_contexual) # Crear el elemento, y asociamos el boton del mouse, en este caso el derecho o inzquierdo
ventana.mainloop()