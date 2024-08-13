---- JOINS----
-- We use two or more tables and mixed them\
--- types of them---

-- CROSS join

SELECT * FROM Employees as e , Orders as o
WHERE e.EmployeeID = o.EmployeeID;



-- INNER JOIN
SELECT FirstName, LastName, OrderID FROM Employees as e
INNER JOIN Orders as o ON e.EmployeeID = o.EmployeeID;


--We're going to create a TABLE
-- 
-- CREATE TABLE "Rewards"(  -- The name of the table
-- "RewardID" INTEGER,
-- "EmployeeID" INTEGER,
-- "Reward" INTEGER,
-- "Month" TEXT,
-- PRIMARY KEY("RewardID" AUTOINCREMENT); -- reference to the RewardID;
-- -- We're going to INSERT DATA

-- INSERT INTO Rewards(EmployeeID, Reward, Month) VALUES
-- (3, 200, "January"),
-- (2, 180,"February"),
-- (5, 250, "March"),
-- (1, 280, "April"),
-- (8, 160, "June"),
-- (NULL, NULL, "June");


-- Return just the people who have won money or a Reward 

SELECT FirstName, Reward, Month FROM Employees as e
LEFT JOIN Rewards as r on e.EmployeeID = r.EmployeeID;


-- LEFT JOIN show you from two TABLES, the total information of the first table  and a short information of the second table
-- RIGHT JOIN is the oppositive

-- in this case is like a RIGHT JOIN, WITHOUT especific the word RIGHT, is like a simulation, because in SQL Lite we can't use RIGHT
SELECT FirstName, Reward, Month FROM Rewards as r
LEFT JOIN Employees as e on e.EmployeeID = r.EmployeeID;

-- FULL JOIN, is all the DATA, 
-- This is a simulation fo FULL JOIN using UNION
SELECT FirstName, Reward, Month FROM Employees as e
LEFT JOIN Rewards as r on e.EmployeeID = r.EmployeeID
UNION
SELECT FirstName, Reward, Month FROM Rewards as r
LEFT JOIN Employees as e on e.EmployeeID = r.EmployeeID;


