import tkinter as tk
## Por default lo pone uno debajo del otro
ventana = tk.Tk()
ventana.title("Ejemplo de Pack")
label1 = tk.Label(ventana, text="Ejemplo de Pack1")
label1.pack(side='right', padx = 5) # Aqui ponemos uno despues del otro es decir alado
label2 = tk.Label(ventana, text="Ejemplo de Pack2")
label2.pack(side="left", padx = 5)
ventana.mainloop()