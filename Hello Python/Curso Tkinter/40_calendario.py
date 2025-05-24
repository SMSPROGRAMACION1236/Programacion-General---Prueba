import tkinter as tk
from tkcalendar import Calendar

ventana = tk.Tk()
cal = Calendar(ventana, selectmode='day', locals="es_ES", year=2025, month=10, day=1, date_pattern='dd/mm/yyyy') # Explicacion: selectmode='day' permite seleccionar un dia, locals="es_ES" establece el idioma a español, year=2025 establece el año, month=10 establece el mes de octubre, day=1 establece el dia 1, date_pattern='dd/mm/yyyy' establece el formato de la fecha a dia/mes/año
cal.pack()


def print_date(date):
  print(date)

cal.bind("<<CalendarSelected>>", lambda event: print_date(cal.get_date()))

ventana.mainloop()