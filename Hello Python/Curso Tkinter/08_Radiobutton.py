import  tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de RadioButton!")

#opcion1 = tk.Radiobutton(ventana, text="Opcion 1", font=("Arial", 14),fg = 'blue', bg = 'lightgreen') # aplicamos el radiobutton a la ventana y lo personalizamos
#* Para que tenga mas opciones podemos usar una variable de control
variable_control = tk.IntVar()


opcion1 = tk.Radiobutton(ventana, text="Opcion 1",variable=variable_control,value= 1)
opcion2 = tk.Radiobutton(ventana, text="Opcion 2",variable=variable_control,value= 2)
opcion1.pack()
opcion2.pack()

#* Si queremos que realize algo
def mostrar_seleccion():
    print(f"Opcion Seleccionada: {variable_control.get()}") # imprimira el value 1 o value 2 dependiendo de la seleccion que hagamos

boton = tk.Button(ventana,text="Mostrar Seleccion",command=mostrar_seleccion)
boton.pack()
def cambiar_color():
    color_seleccionado = variable_control.get() # Obtener el value 1 o 2
    if color_seleccionado == 1:
        ventana.config(bg='lightblue')
    elif color_seleccionado == 2:
        ventana.config(bg='lightgreen')
# * Crear una funcion de tipo radiobutton para personalizar la ventana(color
color1 = tk.Radiobutton(ventana, text="lightblue", variable=variable_control,value=1, command=cambiar_color)
color2 = tk.Radiobutton(ventana, text="lightgreen", variable=variable_control,value=2, command=cambiar_color)
color1.pack()
color2.pack()
ventana.mainloop()

#45:19