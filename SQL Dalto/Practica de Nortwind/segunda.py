"""¿Cuántos empleados nacieron después del 1 de junio de 1965? Crea un informe que diga 
“El empleado Nació el N”, donde “N” representa el nombre completo y la fecha de nacimiento."""
import sqlite3
import pandas as pd

# square = lambda n : n*n
conn = sqlite3.connect("C:\\Users\\santi\\Programación\\Programacion-General---Prueba\\SQL Dalto\\Practica de Nortwind\\Northwind.db") 
# conn.create_function('SQUARE', 1, square)

courser = conn.cursor()
courser.execute("""
                SELECT FirstName,BirthDate FROM Employees WHERE BirthDate > '1965-06-01'""")
result = courser.fetchall()

conn.commit()
courser.close() 
conn.close()  
result_pd = pd.DataFrame(result)
print("El empleado nacio el")
print(result_pd)

