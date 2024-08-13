--- 1. Clientes y Pedidos
-- Cuantos clietes hay registrados en la tabla "Customers"

SELECT count(CustomerName)  as client_number FROM Customers;


-- Cuantos pedidos existen en la tabla Orders
SELECT count(OrderId) orders_numbers from Orders;

-- Cual es el nombre de los clientes que viven en londres y cuyo nombre(campo "CustomerName") comienza con la letra 'A"
SELECT * FROM Customers
WHERE City = "London" and CustomerName like "A%";
-- Cuantos clientes son de londres en total

SELECT count(CustomerName) as clients_in_london from Customers
WHERE city = "London" ;

-- Cuantas clientes hay en cada ciudad
SELECT  (SELECT count(CustomerName) FROM Customers WHERE city = "London" ) as london,
(SELECT count(CustomerName) FROM Customers WHERE city = "Berlin" ) as berlin,
(SELECT count(CustomerName) FROM Customers WHERE city = "Madrid" ) as madrid
FROM Customers
LIMIT 1;

---- 2. Empleados
--¿Cuántos empleados nacieron después del 1 de junio de 1965? Crea un informe que diga 
--“El empleado Nació el N”, donde “N” representa el nombre completo y la fecha de nacimiento.

SELECT FirstName || ' ' || LastName AS 'Nombre Completo', BirthDate AS 'Nació el'
FROM Employees
WHERE BirthDate > "1965-06-01";


--Repite el informe anterior, pero solo para los empleados con los ID 8, 7, 3 y 10.

SELECT FirstName || ' ' || LastName AS 'Nombre Completo', BirthDate AS 'Nació el'
FROM Employees 
WHERE BirthDate > "1965-06-01" AND EmployeeID  in (8, 7, 3, 1);

--¿Cuáles son los países que tienen más de 5 clientes? 
--Ordénalos alfabéticamente por nombre de país.

SELECT  COUNT(*) AS CantidadClientes
FROM Customers
GROUP BY Country
;


SELECT Country, (SELECT  COUNT (Country)
FROM Customers) AS CantidadClientes
FROM Customers
GROUP by Country