import  tkinter as tk


def on_click(event):
    print(f"{event.widget['text']} presionado")


ventana= tk.Tk()
buttons = [tk.Button(ventana, text= f"Boton{i}") for i in range(3)] # creamos 3 botones usando listas de comprension

for button in buttons:
    button.pack() # iteramos en la lista de botones para empaquetar cada boton en la ventan
    button.bind("<Button-1>", on_click) # cata boton sera asociado con el click izquierdo
ventana.mainloop()
