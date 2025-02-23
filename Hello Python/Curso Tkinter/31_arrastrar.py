
import tkinter as tk

def iniciar_arrastre(event):
  global objeto_seleccionado
  objeto_seleccionado = canvas.find_closest(event.x, event.y)
  
def terminar_arrastre(event): # Funcion que se activa cuando se suelta el boton izquierdo del mouse y se le pasa el evento event como parametro 
  global objeto_seleccionado
  if objeto_seleccionado:
    x, y = event.x, event.y # Se obtienen las coordenadas del mouse en el evento
    canvas.move(objeto_seleccionado, x- canvas.coords(objeto_seleccionado)[0], y- canvas.coords(objeto_seleccionado)[1]) # Se mueve el objeto seleccionado a las coordenadas del mouse 
    objeto_seleccionado = None
ventana = tk.Tk()

canvas = tk.Canvas(ventana, width=500, height= 300)
canvas.pack()


objeto_seleccionado = None # Variable global que nos permitira saber si un objeto esta seleccionado o no, None es para que no haya nada seleccionado al principio del programa

rectangule = canvas.create_rectangle(50, 50, 100, 150, fill="green", outline="black", width=2, tags='rectangule') # (los dos primeros son coordenadas, y los otros dos son el tamaño)


canvas.tag_bind("rectangule", "<ButtonPress-1>", iniciar_arrastre) # <ButtonPress-1> es un evento que se activa cuando se presiona el boton izquierdo del mouse, y se le pasa la funcion iniciar_arrastre
canvas.tag_bind("rectangule", "<ButtonRelease-1>", terminar_arrastre) # <ButtonRelease-1> es un evento que se activa cuando se suelta el boton izquierdo del mouse, y se le pasa la funcion terminar_arrastre

ventana.mainloop()