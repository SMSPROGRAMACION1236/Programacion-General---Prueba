import  tkinter as tk

ventana = tk.Tk()
decimal = tk.DoubleVar(value= 3.14)
control_deslizante = tk.Scale(ventana, variable= decimal, from_=0, to= 10, resolution= 0.01, orient= tk.HORIZONTAL) # Es una barra para deslizar que va desde 0 a 10, y se mueve de 0,01 a 0,01 de manera horizontal

control_deslizante.pack()

ventana.mainloop()