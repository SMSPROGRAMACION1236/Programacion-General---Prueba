import  tkinter as tk
ventana = tk.Tk()

ventana.title("Ejemplo de entry")

etiqueta = tk.Label(ventana, text="Lo de abajo es un entry:")
etiqueta.pack()

entrada = tk.Entry(ventana) # se le aplica el entry a la ventana
#*personalizacion del entry
entrada.config(fg= "green" , bg="yellow",font=("Arial",13)) # color de fondo y color del texto
entrada.pack() # para ponerlo

entrada.insert(1, "Texto por defecto") #  Poner algo por defecto


def cambiar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto) # Con lo introducido en el entry cambiamos el label
boton = tk.Button(ventana, text="Aplicar cambio") # cada vez que lo presionamos podremos cambiar el texto del label
boton.config(command=cambiar_texto)  # te permite que puedas cambiar el texto
boton.pack()
ventana.mainloop()
