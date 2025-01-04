import tkinter as tk
# Un evento es algo que sucede tras la interaccion de un usuario, por ejemplo tras presionar un boton, etc

def on_click(event):
    print("Button clicked!")
ventana = tk.Tk()

button = tk.Button(ventana, text= "Haz clic aqui")
button.pack()
## Asociar un boton con un evento, este caso el boton izquierdo
button.bind("<Button-1>", on_click)  # si se presiona el button se ejecutara el on_click


def on_key_press(event):
    if event.char == 'a': # si el caracter que teclees es igual a "A" hara lo otro
        print("La tecla A ha sido presionada!")

ventana.bind("<KeyPress>", on_key_press)

def on_resize(event):
    print(f"La ventana se ha redimensionado a {event.width}x{event.height}") # imprime las dimensiones de la ventana si es que lo modificamos  o movemos

ventana.bind("<Configure>", on_resize)

def on_mouse_move(event):
    print(f"El mouse se ha movido a {event.x}x{event.y}")  # cada que movemos el mouse imprime las ordenadas
ventana.bind("<Motion>",on_mouse_move)
ventana.mainloop()