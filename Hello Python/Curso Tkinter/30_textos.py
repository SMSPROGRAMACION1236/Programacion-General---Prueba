import tkinter as tk

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=500, height= 300, bg="lightblue") ## Caracteristicas y personalizacion
canvas.pack(fill="both", expand=True) # Nos permite que el canvas se expanda en toda la ventana y se ajuste a ella


canvas.create_text(150, 50, text="Hola Wasaa", fill="darkgreen", font=("Courier", 25, "italic"), justify="center") # los primeros dos son las coordenadas, el tercero es el texto, el cuarto es el color, el quinto es la fuente, el sexto es el tamaño y el septimo es el estilo



canvas.pack()
ventana.mainloop()