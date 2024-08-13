---- Sub Consultas ----\

-- it's about relation the tables,with primary and foreighner keys, it is a consult into a consult

SELECT ProductName FROM Products 
WHERE ProductID = 11;

SELECT name, totally_sell from (SELECT 	ProductID, sum(Quantity) as totally_sell,
		(SELECT ProductName FROM Products WHERE ProductID = OD.ProductID) as Name,
-- This one isn't a sub cosult, it is a operation
		(sum(Quantity) * (SELECT Price FROM Products WHERE ProductID = OD.ProductID)) as totally_earn
FROM OrderDetails as OD
WHERE (SELECT Price FROM Products WHERE ProductID = OD.ProductID) >40 -- We use a subconsult to compare with a value
GROUP by ProductID
ORDER by  totally_earn )WHERE totally_sell > 100;
-- To see the Employees that sell the most quantities of thing, is like units

SELECT FirstName, LastName,
(SELECT sum(od.Quantity)FROM [Orders] o, [OrderDetails] od
WHERE o.EmployeeID = e.EmployeeID AND od.OrderID = o.OrderID
) as totally_units
FROM [Employees]  e
WHERE totally_units < (SELECT avg(totally_units)FROM(
SELECT (SELECT sum(od.Quantity)FROM [Orders] o, [OrderDetails] od
WHERE o.EmployeeID = e2.EmployeeID AND od.OrderID = o.OrderID) as totally_units from Employees  as e2
GROUP by e2.EmployeeID
))