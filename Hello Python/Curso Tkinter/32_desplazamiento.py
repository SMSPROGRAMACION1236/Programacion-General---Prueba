import tkinter as tk


ventana = tk.Tk()
scrollbar_vertical = tk.Scrollbar(ventana) # Crear un scrollbar vertical en la ventana
scrollbar_vertical.pack(side="right", fill="y") # Empaquetar el scrollbar en la ventana en el lado derecho, fill en y para que se expanda en el eje y (vertical)

ventana.mainloop()