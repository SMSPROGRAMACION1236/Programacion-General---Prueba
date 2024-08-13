---- UNION , UNION ALL ----


-- Union is to mix consults(the tables that return from the consults) with the same amount of columns and type of DATA


SELECT FirstName, Reward, Month FROM Employees as e
LEFT JOIN Rewards as r on e.EmployeeID = r.EmployeeID
UNION ALL
SELECT FirstName, Reward, Month FROM Rewards as r
LEFT JOIN Employees as e on e.EmployeeID = r.EmployeeID;


--- Cardinally ---
--Types

-- One to One(1:1)--
-- One data to another data from different TABLES, example, a person with his ID
-- One to a lot(1:n) --
-- one data to a lot of datas from different TABLES, One to a lot of datas example, a writer with a lot of books
-- A lot to a lot --
-- A lot of data to alot data from different TABLES, example, one student can do many courses, and each course has many students too, we use a middle class to be more easy



