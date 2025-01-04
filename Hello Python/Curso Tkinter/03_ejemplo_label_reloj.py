import  time # te permite usar la hora
import  tkinter as tk

ventana = tk.Tk()

ventana.title("Ejemplo de Reloj con Label")

etiqueta = tk.Label(ventana, text="Ejemplo de Reloj con Label") # nueva etiqueta en la
etiqueta.pack()

def actualizar_reloj():
    etiqueta.config(text=time.strftime("%H-%M-%S")) # cambiar el texto anterior con la hora, usando la libreria time y su formato
    ventana.after(1000,actualizar_reloj) # metodo after, te permite ejecutar algo cada cierto tiempo en este caso cada 1(1000 milisegundos)
actualizar_reloj()

ventana.mainloop()