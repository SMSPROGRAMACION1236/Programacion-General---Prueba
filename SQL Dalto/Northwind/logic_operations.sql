-- Logic Operations

-- AND both or all of the ANDs must be True 
SELECT * FROM Customers
WHERE CustomerID >= 50 AND CustomerID <55;

-- OR we use when it can be a tring or another one, where one of them need to be execute 
SELECT * FROM Employees
WHERE FirstName = "Nancy" OR FirstName = "Anne";

-- Using both of them, when we use them we need tu put () because it' d be like  n OR(n AND n) "Just a put parentesis to undestand  better, withot ir it'be like it and in this case we need (n OR n) AND n
SELECT * FROM Products
WHERE (Price < 20 or CategoryID = 6) AND SupplierID = 7;
-- to denay  a conditional
SELECT * FROM Products
WHERE NOT Price > 40;
-- A good use of NOT
SELECT * FROM Customers
WHERE NOT Country = "USA";

--using And and NOT
SELECT * FROM Customers
WHERE not Country = "USA" AND NOT Country = "France" AND Country = "Brazil"
-- We use a limit in this case just 5 lines
LIMIT 5;
-- we have  a lot of buts that a person gave us it doesn't like meat(CategoryID = 6) and also the seller (SupplierID = 1) and it need cost less than 30 dollars and  we have just tell him 3 ones at random

SELECT * FROM Products
WHERE NOT CategoryID = 6
AND NOT  SupplierID = 1
AND Price <= 30
ORDER BY random()
LIMIT 3;
-- NOT is a logic operation
-- != is a operation to compare
SELECT * FROM Customers WHERE  Country != "USA";

-- --BETWEEN ------
-- Rules
-- -- The first value must be biggest that the second VALUE
-- -- We use it just data with the same DATABASE
SELECT * from Products
--  It retuern you a range of princes just in this case because it has a lot of uses
WHERE Price BETWEEN 20 and 40;

SELECT * FROM Employees
WHERE BirthDate BETWEEN "1968-0-1" and "1970-0-1";

SELECT * FROM Employees 
WHERE EmployeeID BETWEEN 2 AND 6 ; -- These ones put the limits in this case 2 and 6 and the values between these ones

------like ------

-- To look something some string
-- Is similar a "="


SELECT * FROM Employees 
WHERE LastName like "Fuller";

---% it means  we say it can be something behind a character if the % is first but if there are the character and then the % will be the opposite
SELECT * FROM Employees
WHERE LastName like "%io" ; -- it need to finish with io but it can be somewords behind it


SELECT * FROM Employees
WHERE LastName like "fu%";  -- Something start with fu and the finish with another letters 
-- We can use it when it start and end, it meaning, that it works just if it has in this case r BETWEEN some letters at random
SELECT * FROM Employees
WHERE LastName like "%r%";
-- _ we use _ to put the letter or letters to start and the letter or letters to end and BETWEEN them we put _ considering the numbers of missing letters or characters

SELECT * FROM Employees
WHERE LastName like "F____r";

-- but we also use it WITHOUT any specific order
SELECT * FROM  Employees
WHERE LastName like "Full__";

-- we can use % and _ in the same one

SELECT  * FROM Employees
WHERE LastName like "_u___%";

-- is_nulll

SELECT * FROM Products
WHERE ProductName Is NOT NULL -- to delete nulls
ORDER by ProductName ASC;

-- In, Not In
-- the operation in is similar or but it shorter one when you have a lot of date to compare
SELECT * FROM Products
WHERE SupplierID In (3, 4, 5, 6); --return the suplient id with thoses numbers

SELECT * FROM Employees
WHERE LastName NOT IN ("Fuller", "King");


--- Add Functions

SELECT count (FirstName)  FROM Employees ;-- it count the numbers of values in the column FirstName into the table Employee

SELECT sum(price) FROM Products ;-- add all the prices of column price into the table Products

SELECT avg(Price) FROM Products; -- to calculate the adverange of something

SELECT round(avg(Price), 2) FROM Products; -- to road something

SELECT ProductName, min(Price) FROM Products -- the min of the prize
WHERE ProductName is NOT NULL;

SELECT ProductName, max(Price) FROM Products
WHERE ProductName is NOT NULL;

--- GROUP BY, HAVING---

-- group is to agroup something in some groups

SELECT SupplierID, round(avg(Price),2) as promedio FROM Products 
GROUP by CategoryID -- using the Categories CategoryID  that is GROUP by it
ORDER BY promedio;

-- having; filter groups is similar where, but we use it with groups
SELECT SupplierID, round(avg(Price),2) as promedio FROM Products 
GROUP by SupplierID -- using the Categories SupplierID  that is GROUP by it
HAVING promedio >40;

SELECT ProductID, sum(Quantity) as Total FROM OrderDetails -- how many times a ticken sold
GROUP by ProductID 
ORDER by Total DESC
LIMIT 1