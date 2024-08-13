-- sirve para renombrar de forma temporal y esto sirve para poner nombre mas faciles y mas accesibles, pero no modifica la tabla original
SELECT LastName As apellido, FirstName AS nombre FROM Employees;
-- that we do is a operation, we times the values times 2
SELECT Price AS precio, Price *2 AS precio_doble FROM Products;

-- Using filter
SELECT * FROM Products
-- filter in the price it grows
ORDER BY Price ASC;
-- filter in the price it doesn't grow, null is the less valua, if so letter> special caracters> numbers>NULL, if so  letter is the most valuable and null its opposite
SELECT * FROM Products
ORDER BY Price DESC; -- is the opposite of ASC\


SELECT * FROM Products
-- now is in the alfabet, start in A and fish in Z
ORDER BY ProductName ASC;

SELECT * FROM Products
-- The oppositive
ORDER BY ProductName DESC;


-- we have null, would be like this

SELECT * FROM Products
-- NUlls firts
ORDER By ProductName ASC;

SELECT * FROM Products
-- Null in the last
ORDER BY ProductName DESC;

SELECT * FROM Products
-- if we need null in the last but staying with the function ASC and NULL FISST We use with DESC
ORDER BY ProductName NULLS FIRST;
-- We put at random all the data
SELECT * FROM Products
ORDER BY RANDOM();
-- With DISTINCT we can retunr the TABLE without any repetition
SELECT DISTINCT ProductName FROM Products;

--Condition--
q
SELECT ProductName from Products
-- A way yto say you need the ID 14 from ProductName
WHERE ProductID =  14;
-- Return all the date of the id 23
SELECT * FROM Products
WHERE ProductID = 23;

-- Look for name
SELECT * FROM Products
WHERE ProductName = "Tofu";
-- Put a filter in its price less  40 or the same
SELECT * from Products
WHERE Price <= 40;




