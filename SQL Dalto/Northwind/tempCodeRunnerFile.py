
## The second query(consult) top 10  employees
query2= """FirstName || ' ' || LastName, COUNT(*) as total
        FROM Orders o
        JOIN Employees e
        ON e.EmployeeID = o.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY total DESC"""


top_employees = pd.read_sql_query(query2, conn)

top_employees.plot(x= "Employees", y ="total", kind='bar', figsize=(10,5), legend=False)
plt.title("Top 10 Employee Sales")
plt.xlabel("Employees")
plt.ylabel("Total sold")
plt.xticks(rotation=45)
plt.show()