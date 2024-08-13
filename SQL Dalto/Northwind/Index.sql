----- INDEX ------
-- Desventajas- -
-- Ocupan mucho espacio, y disminuyen el rendimiento,
-- Mas complejos es mantenerlos.  


-- Example:
-- This is normal
SELECT * FROM Products  WHERE ProductName =  "Chais";

-- Now we are going to put an INDEX about it

-- CREATE INDEX name on Products (ProductName);  -- This is the INDEX, if it's CREATE we can't put the same


-- To CREATE un UNIQUE INDEX
--- This one tries there's not any repetition, like, it can't be possible two rows with the same name y surname, to avoid repetitions


-- CREATE UNIQUE INDEX fullname on Employees (FirstName, LastName)


-- Another example
-- Normal one

SELECT * FROM OrderDetails od
INNER JOIN Orders o
WHERE o.OrderID = od.OrderID
AND	OrderDate > "1996-07-04"
AND od.Quantity > 10;

-- CREATE INDEX quantity ON OrderDetails (Quantity);

-- TO DELETE an INDEX, we put DROP and the name of the INDEX(it's not necessary to put the process)

-- DROP INDEX quantity

