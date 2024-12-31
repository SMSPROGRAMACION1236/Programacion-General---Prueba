import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

### We connect to the DB
conn = sql.connect("C:/Users/santi/Programación/SQL Dalto/Northwind/Northwind.db")
## The first query(consult), top ten products
query ="""SELECT ProductName, SUM(Price * Quantity) AS Revenue
FROM OrderDetails od
JOIN Products p ON p.ProductID = od.ProductID
GROUP BY od.ProductID
ORDER BY  Revenue DESC
LIMIT 10"""

top_products = pd.read_sql_query(query, conn)
top_products.plot(x="ProductName", y=["Revenue"], kind='bar', figsize= (10,5), legend=False)
plt.title("Ten Best Sellers")
plt.xlabel("Products")
plt.ylabel("Renevue")
plt.xticks(rotation = 90)
plt.show()



## The second query(consult) top 10  employees
query2= """SELECT FirstName ||""|| LastName as Employee, COUNT(*) as total
        FROM Orders o
        JOIN Employees e
        ON e.EmployeeID = o.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY total DESC"""


top_employees = pd.read_sql_query(query2, conn)

top_employees.plot(x="Employee", y=["total"], kind='bar', figsize= (10,5), legend=False)
plt.title("Top 10 Employee Sales")
plt.xlabel("Employees")
plt.ylabel("Total sold")
plt.xticks(rotation=45)
plt.show()