import tkinter as tk

ventana = tk.Tk()  # para crear la primera ventana, y asi llamamos a la clase de Tkinter
ventana.title("Mi primera ventana")  # le damos un título a nuestra ventana

#* Para poner las dimensiones de la ventana
ventana.geometry("600x200+400+300")  # Tamaño de la ventana, y tambien la ubicación de la ventana(coordenadas)
ventana.minsize(200, 100)  # poner un minimo al usuario para achicar
ventana.maxsize(800, 400)  # poner un máximo al usuario para achicar
ventana.iconbitmap("tkinterexample.ico")  # para poner un icono a la ventana, debe ser .ico
ventana.configure(bg="sky blue")  # color del fondo
ventana.resizable(False, False)  # si ambos estan false, no te permite redimensionar el tamaño
ventana.attributes("-alpha", 0.4) # transparencia de la ventana
ventana.mainloop()  # con esto creamos la ventana como tal
