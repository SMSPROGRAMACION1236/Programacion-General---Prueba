# User Defined functions

### it's a function used by sql lite, but can be used in other databases as well. we need to create it in another language, but  put in sql

import sqlite3
import pandas as pd
## This is one is a transtation #TODO Check it
## First we need to create the function

square = lambda n : n*n# Take n and it'll return us n*n
conn = sqlite3.connect("C:/Users/santi/Programación/SQL Dalto/Northwind/Northwind.db"SELECT * FROM CustomersSELECT * FROM Customers) # To connect to the database

## Second we're going to put in SQL

conn.create_function('SQUARE', 1, square) # The first one is the name of the function in sql, the second one is the numbers of pParameter, and the third one is the function to use

## Third

courser = conn.cursor()
courser.execute("""
                SELECT * FROM Employees
                where Birt""")
result = courser.fetchall() # To get the information

## To keept it, we need to do a commit
conn.commit()  # We make sure, the information is sure

## After it we need to close it
courser.close() # Liberate the resources
conn.close()  # Closed the  connection with the DBMS
result_pd = pd.DataFrame(result)
print(result_pd)