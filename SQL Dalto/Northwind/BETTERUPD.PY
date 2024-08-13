## We need to import sql and pandas

import  sqlite3 as sql
import pandas as pd
## In this case, the conexion closes in a auto way
square = lambda n : n*n

with sql.connect("C:/Users/santi/Programación/SQL Dalto/Northwind/Northwind.db") as conn:
  conn.create_function("SQUARE", 1, square)
  cursor = conn.cursor()
  cursor.execute("""SELECT * FROM Products""")
  results = cursor.fetchall()
  resuld_df = pd.DataFrame(results)
print(resuld_df)


### But the better form is using catch  exceptions
