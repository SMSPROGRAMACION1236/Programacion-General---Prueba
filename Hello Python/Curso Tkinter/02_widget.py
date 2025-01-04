import tkinter as tk

ventana = tk.Tk()

ventana.title("Ejemplo de Label") # titulo

etiqueta = tk.Label(ventana,text="Ejemplo de Label") # la primera etiqueta del label,  y queremos que se coloque en la ventana y le ponemos un texto
etiqueta.config(text="Nuevo Texto") # Una forma de reescribir el texto
etiqueta.config(fg = "blue", bg = "white",font =("Arial",14, "bold")) # Color del texto y su fuente, tipo de letra,  tamaño de la letra y el tipo de tipografia

etiqueta.pack() # para que podamos verlo y lo pondra en la ventana

ventana.mainloop()
