import tkinter as tk

ventana = tk.Tk()

ventana.title("Ejemplo de Place")

label1 = tk.Label(ventana, text="Ejemplo de Place1")
# label1.place(x=50, y=50) # Es la cordenada exacta
label1.place(relx=0.5, rely=0.25) # Se usa el porcentaje
label2 = tk.Label(ventana, text="Ejemplo de Place2")
label2.place(relx=0.5, rely=0.5) # se usa el porcentaje
# label2.place(x=150, y=150) # Es la cordenada exacta
ventana.mainloop()