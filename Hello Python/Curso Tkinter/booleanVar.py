import  tkinter as tk

ventana = tk.Tk()

booleano = tk.BooleanVar(value= True)

casilla = tk.Checkbutton(ventana, text="Aceptar", variable= booleano)
casilla.pack()

def actualizar(*args):
    print(booleano.get()) # Imprimira el valor de la casilla que sera almacenado en booleano, que sera True o False
booleano.trace("w",actualizar) # w detecta los cambios, ejecuta algo tras detectar un cambio.

ventana.mainloop()