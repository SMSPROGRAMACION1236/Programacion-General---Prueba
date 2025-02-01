import tkinter as tk
from PIL import Image, ImageTk
from PIL import ImageFilter

ventana = tk.Tk()

etiqueta = tk.Label(ventana)
## Nos permite usar formatos jpg
image_pil = Image.open("imagen.png") #! No funciona, no abre la imagen
imagen_redimencionada = image_pil.resize((50, 50))
imagen_rotada =  imagen_redimencionada.rotate(90)

imagen_tk= ImageTk.PhotoImage(imagen_rotada)


boton = tk.Button(ventana, image= imagen_tk)
boton.pack()

ventana.mainloop()