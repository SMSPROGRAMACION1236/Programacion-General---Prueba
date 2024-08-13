---- Sub Consultas --

-- it's about relation the tables,with primary and foreighner keys, it is a consult into a consult

SELECT 	ProductID, -- We can't use an alias in a subconsult
		Quantity,
		(SELECT ProductName FROM Products WHERE OD.ProductID = ProductID)  as Name,
		(SELECT Price FROM Products WHERE OD.ProductID = ProductID)  as Price
FROM OrderDetails as OD ; -- we can put an alias

SELECT 	ProductID, sum(Quantity) as totally_sell,
		(SELECT ProductName FROM Products WHERE ProductID = OD.ProductID) as Name,
-- This one isn't a sub cosult, it is a operation
		(sum(Quantity) * (SELECT Price FROM Products WHERE ProductID = OD.ProductID)) as totally_earn
FROM OrderDetails as OD
WHERE (SELECT Price FROM Products WHERE ProductID = OD.ProductID) >40 -- We use a subconsult to compare with a value
GROUP by ProductID
ORDER by  totally_sell;

-- To see the Employees that sell the most quantities of thing, is like units

SELECT sum(od.Quantity) FROM [Orders] o, [OrderDetails] od