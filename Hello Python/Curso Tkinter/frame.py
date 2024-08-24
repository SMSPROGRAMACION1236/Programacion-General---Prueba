## Cuadros o contenedores para poner cosas

import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("500x300")
ventana.configure(bg="sky blue")  # color del fondo

frame1 = tk.Frame(ventana)  # En donde el frame, en este caso aplicara a ventana
frame1.configure(width=300, height=200, bg="red", bd=5)  # Dimensiones, color de fondo y borde de 5

frame2 = tk.Frame(frame1)  # En donde el frame, en este caso aplicara a otro frame
frame2.configure(width=100, height=50, bg="black", bd=5)  # Dimensiones, color de fondo y borde de 5
frame1.pack()  # para que se vea en la ventana
frame2.pack()  # para que se vea en el frame1

ventana.mainloop()