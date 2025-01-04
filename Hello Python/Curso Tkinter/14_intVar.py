import  tkinter as tk

ventana = tk.Tk()

ventana.title("Ejemplo de IntVar")

entero = tk.IntVar(value=21)
# print(entero.get()) # imprimir el valor
entero.set(value=31)
# print(entero.get()) # imprimir el nuevo valor
opcion1 = tk.Radiobutton(ventana, text="Opcion 1",variable= entero, value=1)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="Opcion 2",variable= entero, value=2)
opcion2.pack()

def actualizar(*args):
    print(entero.get()) # imprimir el valor de entero
entero.trace("w",actualizar) # cada vez que seleccionamos algo ya sea opcion 1 o opcion2, su valor sera guardado en entero
ventana.mainloop()