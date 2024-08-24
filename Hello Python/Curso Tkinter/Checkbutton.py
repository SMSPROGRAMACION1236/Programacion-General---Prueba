import tkinter as tk

ventana = tk.Tk()

variable_check1 = tk.BooleanVar()  # True o False
variable_check2 = tk.BooleanVar()  # True o False


# * Por cada check necesitamos un variable
def on_checkbutton():  # !Corregir
    if variable_check1.get() == True:
        print("Check1 activado")
    elif variable_check2.get() == True:
        print("Check2 activado")
    elif variable_check1.get() == False:
        print("Check1 desactivado")
    elif variable_check2.get() == False:
        print("Check2 desactivado")


def habilitar():
    if variable_check1.get():
        boton.config(state='normal')
    else:
        boton.config(state='disabled')


check1 = tk.Checkbutton(ventana, text="Check1", font=("Arial", 30), bg="violet", fg='red', variable=variable_check1,
                        command=habilitar)
check2 = tk.Checkbutton(ventana, text="Check2", font=("Arial", 30), bg="brown", fg='blue', variable=variable_check2,
                        command=habilitar)  # ! No funciona las funciones

check1.pack()
check2.pack()
boton = tk.Button(ventana, text="Botón", font=("Arial", 30), bg="green", fg='white', state='disabled')
boton.pack()
ventana.mainloop()
