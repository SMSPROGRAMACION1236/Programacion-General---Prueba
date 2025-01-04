import  tkinter as tk

ventana = tk.Tk()

texto = tk.StringVar(value="Hola SMS")  # Le damos un valor por defecto
# print(texto.get()) # para imprimir
texto.set(value="Bye SMS") # Le cambiamos de valor
# print(texto.get()) #Para imprimir

entrada = tk.Entry(ventana, textvariable= texto)
entrada.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

def cambiar_etiqueta(*args):
    etiqueta.config(text=texto.get())
texto.trace("w", cambiar_etiqueta)  # trace detecta cada cambio que ocurre en texto
ventana.mainloop()
