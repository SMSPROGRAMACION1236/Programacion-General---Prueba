import  tkinter as tk

ventana = tk.Tk()

ventana.title("Ejemplo de Boton")

boton = tk.Button(ventana, text="Presiona Aqui") # se crea un boton con el texto presiona aqui

boton.config(fg = "blue", bg = "white",font =("Arial",14)) # personalizacion del boton
#* Para que el boton realize algo
boton.pack()
etiqueta =tk.Label(ventana, text="Soy un Label")
etiqueta.pack()
def cambiar_texto():
    etiqueta.config(text="Presionado") # De soy un label a Presionado

boton.config(command=cambiar_texto) # para que cuando se presione el boton, se ejecute la funcion presionado()




ventana.mainloop()