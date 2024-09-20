import tkinter as tk

from tkinter.scrolledtext import ScrolledText # Te permite hacer este tipo de wigget

ventana = tk.Tk()
#El texto se ajustara mediante a las palabras que se ponga mediante wrap = 'word'
texto = tk.Text(ventana, height=10, wrap="word",bg="gray",fg="black",=10, pady=10, font=( "Arial", 12)) # Ubicar un texto sin desplazamiento

## Agregar  predeterminado
texto.insert("1.0", "Bienvenido al Editor de Texto") # Ponemos en que linea, en este caso en el primero
texto.insert("end","\n\nEste es un ejemplo de texto resaltado", 'resaltado') # podemos al final
## Agregar color
texto.tag_configure("resaltado", background="yellow",foreground="black")
## Imprimir el contenido  dentro del editor de texto
contenido = texto.get("1.0","end") # Elegimos el rango desde la linea 1 al final
print(contenido)
texto.delete("2.0", 'end') # Borrar desde la linea 2 al final
texto.pack() # lo ponemos en la ventana

texto_desplazable = ScrolledText(ventana) # texto con desplazamiento
texto_desplazable.pack()

ventana.mainloop()