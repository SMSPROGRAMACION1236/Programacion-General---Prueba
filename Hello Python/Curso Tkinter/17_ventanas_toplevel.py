import tkinter as tk

ventana = tk.Tk()

ventana.title("Ventana Principal")

ventana.geometry("600x200")




def abrir_ventana_toplevel(): # Al presionar el boton, se abre la ventana toplevel
  global ventana_toplevel 
  ventana_toplevel = tk.Toplevel(ventana)
  #*Caracteristicas de la ventana
  ventana_toplevel.title("Ventana Toplevel")
  ventana_toplevel.geometry("300x200+50+50")
  label = tk.Label(ventana_toplevel,text="Ventana Toplevel")
  label.pack()
  
boton = tk.Button(ventana, text="Abrir ventana top level", command=abrir_ventana_toplevel)
boton.pack()


# def cerrar_ventana_top_level(ventana):
#   ventana.destroy()
# boton = tk.Button(ventana,text="Cerrar topLevel", command=cerrar_ventana_top_level(ventana_toplevel))
# boton.pack()


ventana.mainloop()
