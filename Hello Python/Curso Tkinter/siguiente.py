import tkinter as tk

def copiar():
  texto.event_generate("<<Copy>>") # Asociamos algo al boton de copiar
def cortar():
  texto.event_generate("<<Cut>>") # Asociamos algo al boton de cortar
def pegar():
  texto.event_generate("<<Paste>>")  # asociamos algo al boton de cortqar
  
ventana = tk.Tk()

texto = tk.Text(ventana)
texto.pack()

## Configuramos los botones con las acciones de copiar, pegar y cortar
boton_copiar = tk.Button(ventana, text="Copiar", command=copiar)
boton_copiar.pack()
boton_cortar = tk.Button(ventana, text="Cortar", command=cortar)
boton_cortar.pack()
boton_pegar = tk.Button(ventana, text="Pegar", command=pegar)
boton_pegar.pack()

ventana.mainloop()