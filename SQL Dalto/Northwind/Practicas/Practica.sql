-- Practice about operations


SELECT * from Employees
WHERE (EmployeeID = 2 or EmployeeID = 7) and( LastName = "King");

SELECT LastName as apellido FROM Employees
WHERE apellido = "King";


SELECT * FROM Orders
ORDER by CustomerID ASC;

SELECT * FROM Orders
ORDER by NOT CustomerID = 2;

SELECT * FROM Orders
ORDER by ShipperID DESC;

SELECT * FROM Orders
WHERE CustomerID > 60 AND NOT ShipperID  = 1 AND EmployeeID < 4;
-- order by random WHERE CustomerID AND EmployeeID are different
SELECT * FROM Orders
WHERE CustomerID != 2 AND EmployeeID != 2
ORDER by random();
-- find a specific thing
SELECT CategoryName as name FROM Categories
WHERE CategoryName ="Produce";
SELECT CategoryName as name FROM Categories
WHERE CategoryName !="Produce";

SELECT * FROM Products
WHERE  NOT ProductName ISNULL AND (SupplierID = 1 AND CategoryID = 1)
ORDER by NOT Price ASC
LIMIT 1;

SELECT * FROM Customers
WHERE CustomerID NOT BETWEEN 10 and 19 ;


SELECT * FROM Customers
WHERE City like "Berlin";
-- INSERT INTO Customers(CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
-- VALUES
-- (93,"Elias Gonzales","EliasPro 43", "24, San Lorenzo", "Capiata", 434353, "Paraguay")



SELECT * fROM Customers
WHERE Country == "Paraguay"
ORDER by random()
LIMIT 1;

SELECT round(sum(price),1) as total_price FROM Products 
WHERE SupplierID != 1 and SupplierID != 2;

SELECT * FROM Suppliers
GROUP by Country
HAVING Country = "USA";

SELECT  * FROM Suppliers
WHERE Country = "USA"
ORDER by random()
limit 2;

-- Subconsults

SELECT CategoryID,
(SELECT CategoryName FROM Categories WHERE big.CategoryID = CategoryID)as  CategoryName,
(SELECT Description FROM Categories WHERE big.CategoryID = CategoryID) as Description
FROM Products as big
WHERE CategoryID is not null