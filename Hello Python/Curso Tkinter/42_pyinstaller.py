import tkinter as tk


def mostrar_mensaje():
    mensaje = "Hola, este es un mensaje de prueba."
    etiqueta.config(text=mensaje)
ventana = tk.Tk()
ventana.title("Ejemplo de Tkinter")
ventana.geometry("300x200")


etiqueta = tk.Label(ventana, text="Haz clic en el botón para ver un mensaje.")
etiqueta.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()