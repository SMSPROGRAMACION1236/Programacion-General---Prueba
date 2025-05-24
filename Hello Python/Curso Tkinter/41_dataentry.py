import tkinter as tk
from tkcalendar import DateEntry

ventana = tk.Tk()


date_entry = DateEntry(ventana, selectmode='day', locale='es_ES', year=2025, month=10, day=1, date_pattern='dd/mm/yyyy') # Explicacion: selectmode='day' permite seleccionar un dia, locale='es_ES' establece el idioma a español, year=2025 establece el año, month=10 establece el mes de octubre, day=1 establece el dia 1, date_pattern='dd/mm/yyyy' establece el formato de la fecha a dia/mes/año
date_entry.set_date('01/10/2025') # Establece la fecha inicial en el DateEntry


date_entry.bind("<<DateEntrySelected>>", lambda event: print(date_entry.get_date())) # Imprime la fecha seleccionada en el DateEntry

date_entry.pack()

ventana.mainloop()