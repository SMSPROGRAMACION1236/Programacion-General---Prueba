import tkinter as tk

ventana = tk.Tk()

canvas = tk.Canvas(ventana, width=500, height= 300, bg="lightblue") ## Caracteristicas y personalizacion

##* Crear canvas
rectangule = canvas.create_rectangle(50, 50, 100, 150, fill="green", outline="black", width=2, tags='rectangule') # (los dos primeros son coordenadas, y los otros dos son el tamaño)

canvas.move(rectangule, 100, 100)
oval = canvas.create_oval(200, 50, 250, 150, fill="red", outline="black", width=2, tags='oval')
line = canvas.create_line(350, 50, 400, 150, fill="blue", width=2, tags='line', capstyle="round") # capstyle: round, butt, project
poly = canvas.create_polygon(450, 50, 500, 150, 400, 150, fill="yellow", outline="black", width=2,dash=(5,2), tags='poly')
canvas.pack(fill="both", expand=True) ## Nos permite que el canvas se expanda en toda la ventana y se ajuste a ella


ventana.mainloop()