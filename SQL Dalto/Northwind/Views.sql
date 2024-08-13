------ VIEW, a virtual table, is like an reference to a consult ------

-- This is the normal way
SELECT ProductName, ProductID, Price FROM Products
WHERE ProductID > 50
ORDER by ProductID DESC;

-- We create the view, this one, we can use as a TABLE --
-- CREATE VIEW reduced_products as
-- 
-- SELECT ProductName, ProductID, Price FROM Products
-- WHERE ProductID > 20
-- ORDER by ProductID DESC
--- I comment it becuase the VIEW has delated by myself using DROP
-- SELECT * FROM reduced_products
-- limit 4;

-- The bad thing, it has a bad perform

-- The good way to delete and also INDEX is USING if EXISTS

DROP VIEW IF EXISTS reduced_products

