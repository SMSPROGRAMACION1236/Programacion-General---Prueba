import tkinter as tk
ventana = tk.Tk()
ventana.title("Ventana De Grid")
# Creamos dos etiquetas
label1 = tk.Label(ventana, text="Label 1")
label1.grid(row=0, column=0, padx=1, pady=100) # Posiciones de la fila y columna, padx es la distancia de pixeles entre los elementos horzontalmente y pady es verticalemnte
label2 = tk.Label(ventana, text="Label 2")
label2.grid(row=1, column=0, padx=10, pady=10) 

ventana.mainloop()
