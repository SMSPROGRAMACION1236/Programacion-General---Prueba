# Trabaja junto a @compi.py
#! No funciona: No quiere importar las imagenes
import tkinter as tk
ventana  = tk.Tk()
imagen = tk.PhotoImage(file="imagen.png") # Con esto podemos traer imagenes en el tkinter
#imagen2 = tk.PhotoImage(file="imagen2.jpg") #! Solo acepta png y git y no acepta jpg y algunos otros mas.
imagen3 = tk.PhotoIm(file="imagen3.gif") #! Solo acepta png y git y no acepta jpg y algunos otros mas.

etiqueta = tk.Label(ventana, image=imagen)
boton = tk.Button(ventana, image=imagen3)
etiqueta.pack()
boton.pack()


ventana.mainloop()
