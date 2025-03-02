import tkinter as tk


ventana = tk.Tk()
texto = tk.Text(ventana)
scrollbar_vertical = tk.Scrollbar(ventana) # Crear un scrollbar vertical en la ventana
scrollbar_vertical.pack(side="right", fill="y") # Empaquetar el scrollbar en la ventana en el lado derecho, fill en y para que se expanda en el eje y (vertical)



scrollbar_vertical.config(command=texto.yview) # Configurar el scrollbar para que controle el eje y de la ventana de texto, yview es un método de la ventana de texto que devuelve la posición de la ventana de texto en el eje y
texto.config(yscrollcommand=scrollbar_vertical.set) # Configurar la ventana de texto para que el scrollbar controle el eje y
texto.pack(side="left", fill="both", expand=True) # Empaquetar la ventana de texto en la ventana en el lado izquierdo, fill en both para que se expanda en ambos ejes (horizontal y vertical), expand en True para que se expanda en la ventana

ventana.mainloop()